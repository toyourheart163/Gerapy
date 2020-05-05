<template>
	<div class="header-section">
		<div class="pull-right">
			<div id="nav" class="hidden-sm-only">
				<lang-switch></lang-switch>
				<user></user>
			</div>
		</div>
		<div class="hidden-sm-and-up">
			<el-menu
				class="menu"
				router
				mode="horizontal"
				:default-active="$route.path">
				<el-menu-item
					class="menu-list"
					index="/client">
					<span v-text="$lang.menus.clients" class="text"></span>
				</el-menu-item>
				<el-menu-item
					class="menu-list"
					index="/project">
					<span v-text="$lang.menus.projects" class="text"></span>
				</el-menu-item>
				<el-menu-item
					class="menu-list"
					index="/spider">
					<span v-text="$lang.objects.spiders" class="text"></span>
				</el-menu-item>
				<el-submenu index="#">
					<el-menu-item
						class="menu-list"
						index="/task">
						<span v-text="$lang.menus.tasks" class="text"></span>
					</el-menu-item>
					<el-menu-item index="/home">{{ $lang.heads.home }}</el-menu-item>
					<el-menu-item>{{ $store.getters.user }}</el-menu-item>
					<el-menu-item>
						<span @click="onLogout">{{ $lang.buttons.logout }}</span>
					</el-menu-item>
					<el-menu-item><lang-switch></lang-switch></el-menu-item>
				</el-submenu>
			</el-menu>
		</div>
	</div>
</template>

<script>
	import User from './User'
	import LangSwitch from './LangSwitch'

	export default {
		components: {
			User,
			LangSwitch
		},
		methods: {
			onLogout() {
				this.$store.commit('clearToken')
				this.$router.push({path: '/login'})
			}
		}
	}
</script>
