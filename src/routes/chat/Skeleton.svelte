<header class="header bg-body-tertiary">
	<slot name="left" />
	<strong><slot name="title" /></strong>
	<slot name="right" />
</header>
<main>
	<slot name="content" />
</main>

<style lang="scss">
	@import '../main';
	* {
		font-family: 'Outfit', $font-sans-serif;
	}
	.bg-body-tertiary {
		@media (prefers-color-scheme: dark) {
			& {
				background: #333 !important;
			}
		}
	}
	.header {
		padding: 1rem;
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;

		// border-bottom: 1px solid lightgray;

		strong,
		.right,
		.left {
			font-size: 16pt;
		}
	}
</style>
