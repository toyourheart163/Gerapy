<template>
	<div>
		<section class="body-wrap">
			<transition name="fade" mode="out-in">
				<div class="view-page">
					<left class="hidden-s-only"></left>
					<wrapper>
						<router-view></router-view>
					</wrapper>
				</div>
			</transition>
		</section>
	</div>
</template>

<script>
	import Wrapper from '../components/Wrapper'
	import Left from '../components/Left'

	export default {
		name: 'Layout',
		components: {
			Wrapper,
			Left,
		}
	}

</script>

<style lang="scss" scoped>

</style>