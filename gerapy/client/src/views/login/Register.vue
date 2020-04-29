<template>
	<div class="form-container">
		<el-form :rules="rules" label-width="100px" class="form" :model="form" ref="form">
			<div class="title-container">
				<h3 class="title">GerapyHub</h3>
			</div>
			<el-form-item label="用户名" prop="username">
				<el-input v-model="form.username"
					ref="username"
					autocomplete="off"
					@keyup.enter.native="onRegister">
				</el-input>
			</el-form-item>
			<el-form-item label="密码" prop="password">
				<el-input :type="type.password"
					v-model="form.password"
					autocomplete="off"
					@keyup.enter.native="onRegister"
					ref="password">
				</el-input>
				<span class="display" @click="onShowPassword"><span class="el-icon-view"></span></span>
			</el-form-item>
			<el-form-item label="重复密码" prop="password2">
				<el-input :type="type.password"
					v-model="form.password2"
					autocomplete="off"
					@keyup.enter.native="onRegister"
					ref="password2">
				</el-input>
			</el-form-item>
			<el-button type="primary" style="width:100%;margin-bottom:30px;" :loading="loading"
				@click.native.prevent="onRegister">{{ $lang.buttons.register }}
			</el-button>
			<div class="form-user">
					<router-link to="/login">{{ $lang.buttons.login }}</router-link>
			</div>
		</el-form>
	</div>
</template>

<script>

	export default {
		name: 'Register',
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
					username: null,
					password: null,
					password2: null
				},
				rules: {
					username: [{required: true, trigger: 'blur', validator: validateUsername}],
					password: [{required: true, trigger: 'blur', validator: validatePassword}]
				},
				type: {
					password: 'password'
				},
				loading: false
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
			onRegister() {
				if (this.form.password != this.form.password2) {
					this.$message.error(this.$lang.messages.noRepeatPassword)
					return
				}
				this.$refs.form.validate(valid => {
					var form = this.form
					delete form.password2
					if (valid ) {
						this.loading = true
						this.$http.post(this.$store.state.url.user.register,
							form
						).then(() => {
							this.$message.info(this.$lang.messages.registerSuccess)
							this.$router.push({path: '/login'})
							this.loading = false
						}).catch(() => {
							this.loading = false
							this.$message.error(this.$lang.messages.registerFail)
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
