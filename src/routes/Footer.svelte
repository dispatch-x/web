<footer class="py-5 container footer bg-body-tertiary">
	<div class="row">
		<div class="col-lg-3 mb-3">
			<h2 style="font-family: 'Outfit'; " class="icon-link">
				<img alt="Logo" style="height: 48px;" src="/icons/android-chrome-192x192.png" />Dispatch
			</h2>
			<p class="text-muted">
				<!--Find us on <a target="_blank" href="https://github.com/GoneRogueProductions/dispatchx" >Github</a>.
          <br>-->
				Code license
				<a
					target="_blank"
					href="https://github.com/GoneRogueProductions/dispatchx/blob/main/LICENSE">MPL</a
				>, docs
				<a
					href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1"
					target="_blank"
					rel="license noopener noreferrer">CC BY 4.0</a
				>, media
				<a
					href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1"
					target="_blank"
					rel="license noopener noreferrer">CC BY-NC 4.0</a
				>.
			</p>
		</div>

		<div class="col mb-3">
			<h5>Links</h5>
			<ul class="nav flex-column">
				<li class="nav-item mb-2">
					<a href="/" class="nav-link p-0 text-muted">Home</a>
				</li>
				<li class="nav-item mb-2">
					<a href="/authenticate" class="nav-link p-0 text-muted">Log in</a>
				</li>
				<li class="nav-item mb-2">
					<a href="/authenticate?state=reg" class="nav-link p-0 text-muted">Sign up</a>
				</li>
				<li class="nav-item mb-2">
					<a href="/chat" class="nav-link p-0 text-muted">Chat</a>
				</li>
			</ul>
		</div>

		<div class="col mb-3">
			<h5>Contribute</h5>
			<ul class="nav flex-column">
				<li class="nav-item mb-2">
					<a
						target="_blank"
						href="https://github.com/GoneRogueProductions/dispatchx/"
						class="nav-link p-0 text-muted">GitHub</a
					>
				</li>
				<li class="nav-item mb-2">
					<a
						target="_blank"
						href="https://github.com/GoneRogueProductions/dispatchx"
						class="nav-link p-0 text-muted">Issues</a
					>
				</li>
				<li class="nav-item mb-2">
					<a
						target="_blank"
						href="https://github.com/GoneRogueProductions/dispatchx"
						class="nav-link p-0 text-muted">Pull requests</a
					>
				</li>
				<li class="nav-item mb-2">
					<a
						target="_blank"
						href="https://replit.com/@dispatchx/dispatchx-backend"
						class="nav-link p-0 text-muted">API</a
					>
				</li>
			</ul>
		</div>
		<br>
		

		<!-- <div class="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
      <p>© 2022 Company, Inc. All rights reserved.</p>
      <ul class="list-unstyled d-flex">
        <li class="ms-3"><a class="link-dark" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"></use></svg></a></li>
        <li class="ms-3"><a class="link-dark" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#instagram"></use></svg></a></li>
        <li class="ms-3"><a class="link-dark" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#facebook"></use></svg></a></li>
      </ul>
    </div> -->
	</div>
</footer>
<style lang="scss">
	@import 'main';
	footer.footer {
		position: relative;
		bottom: 2rem;
		left: 0;
		text-align: left !important;
		align-items: center;
		justify-content: center;
		display: flex;
		.col,
		.col-lg-3 {
			align-items: center;
			display: flex;
			flex-direction: column;
			ul {
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: center;
			}
		}
		* {
			font-family: 'Outfit', $font-sans-serif !important;
		}
		@media (prefers-color-scheme: dark) {
			& {
				background: #333 !important;
			}
			.text-muted {
				color: $gray-600 !important;
			}
		}
	}
</style>
<script lang="ts">
	import PolicyNavbar from "./policies/PolicyNavbar.svelte";
</script>