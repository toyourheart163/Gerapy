<template>
	<div class="form-container">
		<el-form :rules="rules" label-width="100px" class="form" :model="form" ref="form">
			<div class="title-container">
				<h3 class="title">GerapyHub</h3>
			</div>
			<el-form-item label="用户名" prop="username">
				<el-input
					v-model="form.username"
					ref="username"
					@keyup.enter.native="onLogin"
					autocomplete="off">
				</el-input>
			</el-form-item>
			<el-form-item label="密码" prop="password">
				<el-input :type="type.password"
					v-model="form.password"
					autocomplete="off"
					@keyup.enter.native="onLogin"
					ref="password">
				</el-input>
				<span class="display" @click="onShowPassword"><span class="el-icon-view"></span></span>
			</el-form-item>
			<el-button type="primary" style="width:100%;margin-bottom:30px;" :loading="loading"
				@click.native.prevent="onLogin">{{ $lang.buttons.login }}
			</el-button>
			<div class="form-user">
				<router-link to="/register">{{ $lang.buttons.register }}</router-link>
			</div>
		</el-form>
	</div>
</template>

<script>

	export default {
		name: 'Login',
		data() {
			const validateUsername = (rule, value, callback) => {
				if (!value || value.length === 0) {
					callback(new Error(this.$lang.messages.pleaseInputUsername))
				} else {
					callback()
				}
			}
			const validatePassword = (rule, value, callback) => {
				if (!value || value.length === 0) {
					callback(new Error(this.$lang.messages.pleaseInputPassword))
				} else {
					callback()
				}
			}
			return {
				form: {
					username: 'bar',
					password: 'ok',
				},
				rules: {
					username: [{required: true, trigger: 'blur', validator: validateUsername}],
					password: [{required: true, trigger: 'blur', validator: validatePassword}]
				},
				type: {
					password: 'password'
				},
				loading: false,
				redirect: null
			}
		},
		watch: {
			$route: {
				handler(route) {
					this.redirect = route.query && route.query.redirect
				},
				immediate: true
			}
		},
		methods: {
			onShowPassword() {
				if (this.type.password === 'password') {
					this.$set(this.type, 'password', '')
				} else {
					this.$set(this.type, 'password', 'password')
				}
				this.$nextTick(() => {
					this.$refs.password.focus()
				})
			},
			onLogin() {
				this.$refs.form.validate(valid => {
					if (valid) {
						this.loading = true
						this.$http.post(this.$store.state.url.user.auth,
							this.form
						).then(({data: data}) => {
							this.$store.commit('setToken', data.token)
							this.$store.commit('setUser', this.form.username)
							this.$router.push({path: this.redirect || '/'})
							this.loading = false
						}).catch(() => {
							this.loading = false
							this.$message.error(this.$lang.messages.loginError)
						})
					} else {
						return false
					}
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	@import './form-container';
</style>
