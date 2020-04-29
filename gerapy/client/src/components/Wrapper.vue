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
		<g-footer></g-footer>
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
        return this.width < 415 ? {'is-mobile': true} : {'is-not-mobile': true}
			}
		}
	}
</script>

<style lang="scss">
@import "../assets/scss/components/_vars";

@media screen {
	.is-mobile {
		margin-left: 0px!important;
	}
}

@media screen {
	.is-not-mobile {
		margin-left: calc(100% -#{$sideBarWidth})!important;
	}
}
</style>
