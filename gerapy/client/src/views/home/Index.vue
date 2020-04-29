<template>
	<div>
		<el-row :gutter="20">
			<el-col :xs="24" :sm="24" :lg="8">
				<router-link to="/client">
				<div class="panel">
					<panel-title :title="$lang.objects.client">
						<el-button size="mini" type="primary">
							{{ $lang.buttons.normal }}
						</el-button>
					</panel-title>
					<div class="panel-body" v-loading="loading">
						<h1 class="number">{{ status.success}}</h1>
						<small> {{ $lang.descriptions.normalClients }}</small>
					</div>
				</div>
				</router-link>
			</el-col>
			<el-col :xs="24" :sm="24" :lg="8">
				<router-link to="/client">
				<div class="panel">
					<panel-title :title="$lang.objects.client">
						<el-button size="mini" type="danger">
							{{ $lang.buttons.error }}
						</el-button>
					</panel-title>
					<div class="panel-body" v-loading="loading">
						<h1 class="number">{{ status.error}}</h1>
						<small> {{ $lang.descriptions.errorClients }}</small>
					</div>
				</div>
				</router-link>
			</el-col>
			<el-col :xs="24" :sm="24" :lg="8">
				<router-link to="/project">
				<div class="panel" id="tree">
					<panel-title :title="$lang.objects.project">
						<el-button size="mini" type="success">
							{{ $lang.buttons.normal }}
						</el-button>
					</panel-title>
					<div class="panel-body" v-loading="loading">
						<h1 class="number">{{ status.project }}</h1>
						<small>{{ $lang.descriptions.countProjects }}</small>
					</div>
				</div>
				</router-link>
			</el-col>
		</el-row>
	</div>
</template>
<script>
	import PanelTitle from '../../components/PanelTitle'

	export default {
		data() {
			return {
				radio: '1',
				status: {},
				loading: true,
			}
		},
		components: {
			// ElFormItem,
			PanelTitle
		},
		created() {
			this.getHomeStatus()
		},
		methods: {
			getHomeStatus() {
				this.$http.get(this.$store.state.url.home.status)
					.then(({data: status}) => {
						this.status = status
						this.loading = false
					})
			}
		}
	}
</script>

<style scoped>
	h1.number {
		font-weight: 100;
		margin: 10px 0;
		margin-top: 0;
	}
</style>
