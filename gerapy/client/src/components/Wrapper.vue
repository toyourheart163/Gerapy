<template>
	<div class="main-content ofh" v-bind:class="[isMobile]">
		<g-header></g-header>
		<div class="wrapper">
			<div class="pageContent">
				<el-row>
					<el-col :span="24">
						<slot></slot>
					</el-col>
				</el-row>
			</div>
		</div>
		<g-footer class="hidden-sm-only"></g-footer>
	</div>
</template>

<script>
	import GHeader from './Header'
	import GFooter from './Footer'

	export default {
		name: 'Wrapper',
		components: {
			GHeader,
			GFooter
		},
    data() {return { width: window.innerWidth }},
    mounted() {
      window.addEventListener('resize', () => {
        this.width = window.innerWidth
      })
    },
		computed: {
			isMobile() {
        return this.width < 768 ? {'is-mobile': true} : {'is-mobile': false}
			}
		}
	}
</script>

<style lang="scss">

</style>

