<script defer lang="ts">
	import { onMount } from 'svelte';
	import jQuery from 'jquery';
	import { page } from '$app/stores';
	import { form, field } from 'svelte-forms';
	import { required, email, matchField, min } from 'svelte-forms/validators';
	import fetchIt from '$lib/fetchIt';

	const username = field('username', '', [min(5)]);
	const pass = field('pass', '', [min(8)]);
	const repeatPass = field('repeatPass', '', [matchField(pass), min(8)]);
	let checkBox: boolean = false;
	let checkBxErr: boolean = false;
	const registerForm = form(username, pass, repeatPass);

	function showLogin() {
		jQuery('#loginForm').show();
		jQuery('#regForm').hide();
	}

	function showRegister() {
		jQuery('#loginForm').hide();
		jQuery('#regForm').show();
	}
	function hasProblems() {
		if (checkBox == false) {
			jQuery('#checkBoxErr').show();
			checkBxErr = true;
		} else {
			jQuery('#checkBoxErr').hide();
			checkBxErr = false;
		}
	}

	// Do not refresh on submit, to use AJAX to send request

	onMount(() => {
		hasProblems();
		if ($page.url.searchParams.get('state') == 'reg') showRegister();
		jQuery('#regForm input').on('keyup', function () {
			hasProblems();
		});

		jQuery('#loginForm').submit(function () {
			var username = jQuery('#logInput').text();
			var password = jQuery('#passwInput').text();
			fetchIt('GET', 'https://api.dispatch.eu.org/api/v2/user/${username}/auth', {
				password: password
			});
		});

		jQuery('#loginForm').submit((e) => {
			e.preventDefault();
			var username = jQuery('#logInput').text();
			var password = jQuery('#passwInput').text();
			let response: object = fetchIt(
				'GET',
				'https://api.dispatch.eu.org/api/v2/user/${username}/auth',
				{
					password: password
				}
			);
			localStorage.setItem('session', response.toString());
		});

		jQuery('#regForm').submit((e) => {
			var username = jQuery('#nameInput').text();
			var password = jQuery('#passInput').text();
			fetchIt('GET', 'https://api.dispatch.eu.org/api/v2/users/new', {
				user: username,
				password: password
			});
		});
	});


</script>

<img class="background" alt="Background of nature" src="/backgrounds/bg-1.jpg" />
<div class="login-wrapper-wrapper">
	<div class="login-wrapper">
		<img class="logo" alt="Dispatch logo" src="/icons/android-chrome-192x192.png" />

		<form class="v-stack" id="loginForm">
			<h1 class="login-heading">Sign in</h1>
			<div class="input-group">
				<div class="input-group-text">@</div>
				<div class="form-floating">
					<input
						autocomplete="username"
						type="text"
						name="username"
						class="form-control"
						id="logInput"
						placeholder="username"
					/>
					<label for="logInput">Username</label>
				</div>
			</div>

			<div class="input-group">
				<div class="form-floating">
					<input
						autocomplete="current-password"
						type="password"
						name="password"
						class="form-control"
						id="passwInput"
						placeholder="*******"
					/>
					<label for="passwInput">Password</label>
				</div>
			</div>

			<input type="submit" id="loginButton" value="Sign in" class="d-button login-button" />
			<hr />
			<div style="display: flex; justify-content: baseline;">
				<a class="d-a register-prompt" on:click={showRegister}>No account? Register!</a>
			</div>
		</form>

		<!-- FIXME: weird bugs with error messages + labels -->
		<form class="v-stack" id="regForm" style="display: none;">
			<h1 class="login-heading">Register</h1>
			<div class="input-group">
				<div class="input-group-text">@</div>
				<div class="form-floating">
					<input
						autocomplete="username"
						bind:value={$username.value}
						minlength="5"
						name="username"
						required
						type="text"
						class="form-control"
						id="nameInput"
						placeholder="username"
					/>
					<label for="nameInput">Username</label>
					{#if $registerForm.hasError('username.min')}
						<label style="padding-left: 2px; display: none;" for="nameInput" class="error1"
							>Please use at least 5 characters.</label
						>
					{/if}
				</div>
			</div>

			<div class="input-group">
				<div class="form-floating">
					<input
						autocomplete="new-password"
						bind:value={$pass.value}
						minlength="8"
						name="password"
						type="password"
						class="form-control"
						id="passInput"
						placeholder="*******"
					/>
					<label for="passInput1">Password</label>
					{#if $registerForm.hasError('pass.min')}
						<label style="padding-left: 2px; display: none;" for="passInput" class="error1"
							>Please use at least 8 characters.</label
						>
					{/if}
				</div>
			</div>

			<div class="input-group" style="margin-top: -7px;">
				<div class="form-floating">
					<input
						autocomplete="new-password"
						bind:value={$repeatPass.value}
						minlength="8"
						required
						name="password1"
						type="password"
						class="form-control"
						id="passInput1"
						placeholder="*******"
					/>
					<label for="passInput1">Repeat Password</label>
					{#if $registerForm.hasError('repeatPass.matchField')}
						<label style="padding-left: 2px; display: none;" for="passInput1" class="error1"
							>Please repeat this password.</label
						>
					{/if}
				</div>
			</div>

			<div class="form-check check-box">
				<input
					on:click={hasProblems}
					style="width: auto; aspect-ratio: 1/1;margin-left:0;"
					bind:checked={checkBox}
					required
					class="form-check-input"
					type="checkbox"
					value=""
					id="flexCheckDefault"
				/>
				<label
					on:click={hasProblems}
					style="width: auto; margin-left: 5px;"
					class="form-check-label"
					for="flexCheckDefault"
				>
					I agree to the <a href="/policies/terms">terms and conditions</a>
				</label>
				<label
					style="padding-left: 2px; display: none;"
					for="flexCheckDefault"
					id="checkBoxErr"
					class="error1">Please check this box.</label
				>
			</div>

			<input
				type="submit"
				disabled={!$registerForm.valid || checkBxErr}
				id="registerButton"
				value="Register"
				class="d-button login-button"
			/>
			<hr />
			<div style="display: flex; justify-content: baseline;">
				<a class="d-a register-prompt" on:click={showLogin}>Have an account? Login!</a>
			</div>
		</form>
	</div>
</div>

<style lang="scss">
	@import '../main';

	@import '../../../node_modules/bootstrap/scss/mixins';
	@import '../../../node_modules/bootstrap/scss/functions';
	@import '../../../node_modules/bootstrap/scss/variables';
	@import '../../../node_modules/bootstrap/scss/variables-dark';
	@import '../../../node_modules/bootstrap/scss/maps';
	@import '../../../node_modules/bootstrap/scss/utilities';
	@import '../../../node_modules/bootstrap/scss/root';

	@import '../../../node_modules/bootstrap/scss/progress';
	@import '../../../node_modules/bootstrap/scss/toasts';

	@import '../../../node_modules/bootstrap/scss/forms';

	* {
		font-family: 'Outfit', $font-sans-serif !important;
	}

	.login-heading {
		margin-top: 0;
		text-align: center;
	}
	.logo {
		height: 75px;
		width: auto !important;
		margin-bottom: 0.5rem;
	}

	// Fix dark mode
	.input-group {
		display: flex;
		flex-direction: row;
		box-shadow: $box-shadow-sm;
		@media (prefers-color-scheme: dark) {
			* {
				background: #333 !important;
			}
			.input-group-text {
				border-bottom: 0 !important;
			}
			.form-floating input {
				border-radius: 0 6px 6px 0 !important;
			}
			.form-floating label,
			.form-floating label::after {
				color: $gray-600 !important;
				background: #333 !important;
			}
			.form-floating > .form-control:focus ~ label {
				top: 10px !important;
				padding-top: 0.25rem !important;
			}
		}
		.input-group-text {
			width: auto;
			border: 0;
			background: white;
			border-bottom: 2px solid #dee2e6;
		}
		input {
			outline: none;
			font-family: 'Outfit', $font-sans-serif !important;
			border: 0;
			border-bottom: 2px solid #dee2e6;
		}
	}
	.v-stack {
		gap: 2em;
		width: 80%;
	}
	.login-button {
		font-size: 1.5em;
	}
	.login-button[disabled] {
		background: $gray-600;
		border: 1px solid $gray-700;
		cursor: not-allowed;
		&:hover {
			background: $gray-600;
			border: 1px solid $gray-700;
			box-shadow: 0;
		}
	}
	.register-prompt {
		margin-top: -1em;
		display: initial;
		font-size: 17px;
		width: auto !important;
		text-align: left;
		left: 0;
		position: relative;
	}
	.check-box {
		$check-box-margin: -5px;
		margin-top: $check-box-margin;
		margin-bottom: -15px;
		padding-left: 0;
		@media (prefers-color-scheme: dark) {
			.form-check-input {
				background: #333;
			}
		}
	}

	input.error {
		border-bottom: 2px solid $red;
	}
	label.error {
		color: $red !important;
		margin-top: 52px;
		padding-left: 0;
		background: transparent;
		border: 0;
		z-index: -1;
		transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem);
	}
	.error1 {
		color: $red;
		padding-left: 0;
		padding-top: 5px;
		margin-left: -5px;
		background: transparent;
		border: 0;
		display: block;
		z-index: -1;
		transform: scale(0.85) translateY(-0.5rem) translateX(-1.2rem);
	}

	.login-wrapper {
		height: 100%;
		width: 100%;
		overflow: auto;
		background: white;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		@media (prefers-color-scheme: dark) {
			& {
				color-scheme: dark;
				background: transparent !important;
			}
		}
		margin-top: 2em;
	}
	.background {
		display: none;
		width: 100%;
		height: 100%;
		position: absolute;
		z-index: -2;
		object-fit: cover;
	}

	// Desktop time
	@include media-breakpoint-up(sm) {
		.login-wrapper-wrapper {
			display: flex;
			height: 100%;
			width: 100%;
			position: absolute;
			top: 0;
			left: 0;
			justify-content: center;
			flex-direction: column;
			align-items: center;
			& * {
				width: 100%;
			}
		}
		.login-wrapper {
			padding: 25px;
			border: 2px solid #dee2e6;
			border-radius: 1em 0 0 1em;
			box-shadow: 0 1rem 6rem 20px rgba(0, 0, 0, 0.175);
			max-width: 500px;
			max-height: 575px;
			justify-content: flex-start;
			@media (prefers-color-scheme: dark) {
				& {
					background: #111 !important;
				}
			}
		}
		h1 {
			font-weight: 500;
		}
		.background {
			display: block;
		}
		body {
			padding: 0;
		}
	}

	@include media-breakpoint-up(lg) {
		.login-wrapper {
			padding: 25px;
			margin-left: 10%;
			& * {
				width: 100%;
			}
			border: 2px solid #dee2e6;
			border-radius: 1em 0 0 1em;
			margin: 0;
		}

		.login-wrapper-wrapper {
			display: flex;
			height: 100%;
			width: 100%;
			position: absolute;
			top: 0;
			left: 0;
			justify-content: center;
			align-items: baseline;
			flex-direction: column;
			& * {
				width: 100%;
			}
		}
	}
</style>
