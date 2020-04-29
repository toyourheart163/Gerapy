<template>
	<div>
		<footer class="footer" v-once>Copyright &copy; {{ getYear }} GerapyHub All Rights Reserved. page view times {{ $store.state.path.hit }}
		</footer>
	</div>
</template>
<script>
	export default {
		computed: {
			getYear() {
				return new Date().getFullYear()
      }
    }
	}
</script>
