<script>
	import { page } from '$app/stores';
	import Skeleton from '../Skeleton.svelte';

	var chatId = $page.url.searchParams.get('id');
</script>

<Skeleton>
	<span slot="title">Lorenzo</span>

	<button class="left-button" slot="left"><i class="fa-solid fa-angle-left"></i></button>

	<div class="main" slot="content">
        <form class="message-send bg-body-tertiary">
			<input type="text" autocomplete="off" class="message-input" placeholder="Type your message..." />
			<button type="submit" class="send-button"><i class="fa-solid fa-paper-plane"></i></button>
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
	}


	.message-send {
		position: fixed;
		bottom: 0;
		left: 0;
		width: 100%;
		padding: 1rem;
		display: flex;
	}
	.message-input {
		padding: .25rem;
		border-radius: .5rem;
		border: 1px solid lightgray;
	}
	.send-button {
		position: relative;
	}
</style>
