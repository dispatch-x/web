<script>
	import { page } from '$app/stores';
	import Skeleton from '../Skeleton.svelte';
	import { onMount } from 'svelte';
	import jQuery from 'jquery';

	var chatId = $page.url.searchParams.get('id');

	/* onMount(() => {
		jQuery('.send-button').height(jQuery('.message-input').height().toString());
		jQuery('.send-button').width(jQuery('.send-button').height().toString());
	}); */
</script>

<Skeleton>
	<span slot="title">Lorenzo</span>

	<a href="/chat" class="left-button" slot="left"><i class="fa-solid fa-angle-left" /></a>

	<div class="main" slot="content">
		<form class="message-send bg-body-tertiary">
			<input
				type="text"
				autocomplete="off"
				class="message-input"
				placeholder="Type your message..."
			/>
			<button type="submit" class="send-button"><i class="fa-solid fa-paper-plane" /></button>
		</form>
	</div>
</Skeleton>

<style lang="scss">
	@import '../../main';
	.left-button {
		position: absolute;
		left: 0;
		border: none;
		background: transparent;
		color: $link-color;
		padding: 0 1rem;
		height: 100%;
		font-size: 16pt;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.message-send {
		position: fixed;
		bottom: 0;
		left: 0;
		width: 100%;
		padding: 1rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 1rem;
		@media (prefers-color-scheme: dark) {
			& {
				background: #333 !important;
				color: white;
			}
		}
	}
	.message-input {
		padding: 0.5rem;
		border-radius: 0.5rem;
		border: 1px solid lightgray;
		flex: 1;
	}
	.send-button {
		position: relative;
		border: 0;
		border-radius: 20%;
		background: $primary;
		height: 100%;
		color: white;
		aspect-ratio: 1 / 1;
		padding: 0.5rem 0.65rem;
		display: flex;
		align-items: center;
		justify-content: center;
		min-width: 0;
	}
</style>
