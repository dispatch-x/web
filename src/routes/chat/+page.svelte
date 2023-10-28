<script>
	import Skeleton from './Skeleton.svelte';
	// import Navbar from '../../Navbar.svelte';
	function unixToTime(unix_timestamp) {
		// Create a new JavaScript Date object based on the timestamp
		// multiplied by 1000 so that the argument is in milliseconds, not seconds
		var date = new Date(unix_timestamp);

		// Hours part from the timestamp
		var hours = date.getHours();

		// Minutes part from the timestamp
		var minutes = '0' + date.getMinutes();

		// Seconds part from the timestamp
		var seconds = '0' + date.getSeconds();

		// Will display time in 10:30:23 format
		var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);

		return formattedTime;
	}

	let chats = [
		{
			id: 1034,
			roomName: 'silly billy fam',
			recentMessage: 'George: hello',
			image:
				'https://api.dicebear.com/7.x/rings/svg?seed=George&radius=50&backgroundType=gradientLinear&ringColor=4db6ac,81c784,9575cd,aed581,ba68c8,e57373,f06292,ff8a65,ffb74d,ffd54f,dce775,4dd0e1,7986cb&ringFive=full,half,quarter,eighth&ringFour=half,quarter,full,eighth&ringOne=half,quarter,full,eighth&ringThree=half,quarter,full,eighth&ringTwo=half,quarter,full,eighth&backgroundColor=c0aede,b6e3f4',
			recentTime: 1697902306724,
			notBadge: 2
		},
		{
			id: 1957,
			roomName: 'Lorenzo',
			recentMessage: 'Lorenzo: [GIF] why does this look like iOS?',
			image:
				'https://api.dicebear.com/7.x/rings/svg?seed=Lorenzo&radius=50&backgroundType=gradientLinear&ringColor=4db6ac,81c784,9575cd,aed581,ba68c8,e57373,f06292,ff8a65,ffb74d,ffd54f,dce775,4dd0e1,7986cb&ringFive=full,half,quarter,eighth&ringFour=half,quarter,full,eighth&ringOne=half,quarter,full,eighth&ringThree=half,quarter,full,eighth&ringTwo=half,quarter,full,eighth&backgroundColor=c0aede,b6e3f4',
			recentTime: 1697902306724,
			notBadge: 2
		}
	];
</script>

<Skeleton>
	<span slot="title">Rooms</span>

	<a href="/" class="left-button" slot="left"><i class="fa-solid fa-angle-left" /></a>
	<button class="right-button" slot="right"><i class="fa-solid fa-plus" /></button>

	<div slot="content" class="main">
		{#each chats as chat}
			<a class="chat" href="/chat/view?id={chat['id']}">
				<div>
					<div class="chat-img">
						<sl-avatar image={chat['image']} label={chat['roomName']} />
						<!-- <img src={chat['image']} alt="Logo of {chat['roomName']}" class="lazyload" /> -->
					</div>
					<div class="chat-content">
						<strong>{chat['roomName']}</strong>
						<span class="text-muted">{chat['recentMessage']}</span>
					</div>
				</div>
				<div style="display: flex; flex-direction: column; gap: 5px; align-items: flex-end;">
					<span class="time text-muted">{unixToTime(chat['recentTime'])}</span>
					<div class="badge">{chat['notBadge']}</div>
				</div>
			</a>
			<hr />
		{/each}
	</div>
</Skeleton>

<style lang="scss">
	@import '../main';
	.main {
		.chat {
			@media (prefers-color-scheme: dark) {
				.text-muted {
					color: $gray-600 !important;
				}
			}
			padding: 0.75rem;
			display: flex;
			gap: 10px;
			align-items: center;
			justify-content: space-between;
			cursor: pointer;
			text-decoration: none;
			transition: 0.2s;
			div {
				display: flex;
				align-items: center;
				gap: 10px;
			}
			.chat-img {
				img {
					border-radius: 50%;
					aspect-ratio: 1 / 1;
					height: 48px;
				}
				sl-avatar {
					border-radius: 50%;
					aspect-ratio: 1 / 1;
					height: 48px;
					--sl-color-neutral-400: transparent;
				}
			}
			.chat-content {
				display: flex;
				flex-direction: column;
				gap: 0;
				align-items: baseline;
				justify-content: center;
				color: black;
				@media (prefers-color-scheme: dark) {
					& {
						color: white;
					}
				}
			}
			&:hover {
				background: $gray-200;
			}
		}
		hr {
			margin: 0 !important;
		}
	}

	.right-button {
		position: absolute;
		right: 0;
		border: none;
		background: transparent;
		color: $link-color;
		padding: 0 1rem;
		height: 100%;
		font-size: 16pt;
	}
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
</style>
