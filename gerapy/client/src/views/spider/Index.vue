<template>
	<div class="panel">
		<panel-title :title="$lang.objects.spiders">
			<el-button @click.stop="onRefresh" size="mini">
				<i class="fa fa-refresh"></i>
				{{ $lang.buttons.refresh }}
			</el-button>
		</panel-title>
		<div class="panel-body">
			<el-table
				:data="spiders"
				:empty-text="$lang.messages.noData"
				v-loading="loading"
				:element-loading-text="$lang.messages.loading"
				:style="{width: '100%;'}">
				<el-table-column align="center" prop="name" :label="$lang.columns.name" width="100">
				</el-table-column>
				<el-table-column align="center" prop="project.name" :label="$lang.columns.project" width="100">
				</el-table-column>
				<el-table-column :label="$lang.columns.clients">
					<template slot-scope="scope">
						<el-tag :key="c.id"
							v-for="c in scope.row.client">
							{{c.name}}
						</el-tag>
					</template>
				</el-table-column>
				<el-table-column align="center" :label="$lang.columns.operations" width="100">
					<template slot-scope="scope">
						<el-button
							type="success"
							size="mini" @click="onStartSpiders(scope.row.project.name, scope.row.name, scope.row.client)">
							<i class="fa fa-caret-right"></i>
							{{ $lang.buttons.run }}
						</el-button>
					</template>
				</el-table-column>
			</el-table>
		</div>
	</div>
</template>
<script>
	import PanelTitle from '../../components/PanelTitle'

	export default {
		name: 'SpiderIndex',
		data() {
			return {
				spiders: null,
				clients: null,
				loading: true,
				// to store batch selected id of spider
				spidersStatus: {},
				statusClass: {
					'1': 'success',
					'0': 'warning',
					'-1': 'danger',
				},
				statusText: {
					'1': this.$store.getters.$lang.buttons.normal,
					'0': this.$store.getters.$lang.buttons.connecting,
					'-1': this.$store.getters.$lang.buttons.error,
				}
			}
		},
		components: {
			PanelTitle,
		},
		created() {
			this.onGetSpiderData()
		},
		methods: {
			onRefresh() {
				this.onGetSpiderData()
			},
			onGetClientsStatus() {
				this.clients.forEach((client) => {
					this.onGetClientStatus(client.pk)
				})
			},
			onGetClientStatus(id) {
				this.$set(this.clientsStatus, id, 0)
				this.$http.get(this.formatString(this.$store.state.url.client.status, {
					id: id
				})).then(({data: {result: result}}) => {
					this.$set(this.clientsStatus, id, result)
				}).catch(() => {
					this.$set(this.clientsStatus, id, -1)
				})
			},
			onGetSpiderData() {
				this.loading = true
				this.$http.get(this.$store.state.url.spider.index
				).then(({data: data}) => {
					this.spiders = data.results
					this.loading = false
					// this.onGetClientsStatus()
				}).catch(() => {
					this.loading = false
				})
			},
			// 启动单个任务
			onStartSpider(project, spider, id) {
				this.$http.get(this.formatString(this.$store.state.url.client.startSpider, {
					id: id,
					project: project,
					spider: spider
				})).then(() => {
					this.$message.success(
						this.$store.getters.$lang.messages.successRun
					)
					// this.getJobs()
				}).catch(() => {
					this.$message.error(
						this.$store.getters.$lang.messages.errorRun
					)
				})
			},
			onStartSpiders(project, spider, clients) {
				clients.forEach(client => {
					// console.log(project, spider, client.id)
					this.onStartSpider(project, spider, client.id)
				})
			}
		}
	}
</script>
