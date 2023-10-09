<style lang="scss">
    @import '../main';

    @import '../../../node_modules/bootstrap/scss/mixins';
    @import '../../../node_modules/bootstrap/scss/functions';
    @import '../../../node_modules/bootstrap/scss/variables';
    @import '../../../node_modules/bootstrap/scss/variables-dark';
    @import '../../../node_modules/bootstrap/scss/maps';
    @import '../../../node_modules/bootstrap/scss/utilities';
    @import '../../../node_modules/bootstrap/scss/root';

    @import "../../../node_modules/bootstrap/scss/progress";
    @import "../../../node_modules/bootstrap/scss/toasts";

    @import "../../../node_modules/bootstrap/scss/forms";

    * {
        font-family: 'Outfit', $font-sans-serif!important;
    }

    .login-heading {
        margin-top: 0;
        text-align: center;
    }
    .logo {
        height: 75px;
        width: auto!important;
        margin-bottom: 0.5rem;
    }

    .input-group {
        display: flex;
        flex-direction: row;
        box-shadow: $box-shadow-sm;
        .input-group-text {
            width: auto;
            border: 0;
            background: white;
            border-bottom: 2px solid #dee2e6;
        }
        input {
            outline: none;
            font-family: 'Outfit', $font-sans-serif!important;
            border: 0;
            border-bottom: 2px solid #dee2e6;
        }
    }
    .v-stack {
        gap: 2em;
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
        width: auto!important;
        text-align: left;
        left: 0;
        position: relative;
    }
    .check-box {
        $check-box-margin: -5px;
        margin-top: $check-box-margin;
        margin-bottom: -15px;
        padding-left: 0;
    }

    input.error {
        border-bottom: 2px solid $red;
    }
    label.error {
        color: $red!important;
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
        z-index: -1;
        transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem);
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

<img class="background" src="/backgrounds/bg-1.jpg">
        <div class="login-wrapper-wrapper">
            <div class="login-wrapper">
                <img class="logo" src="/icons/android-chrome-192x192.png">
                
                
                
                <form class="v-stack" id="loginForm">
                    <h1 class="login-heading">Sign in</h1>
                    <div class="input-group">
                        <div class="input-group-text">@</div>
                        <div class="form-floating">
                            <input type="text" name="username" class="form-control" id="logInput" placeholder="username">
                            <label for="floatingInput">Username</label>
                        </div>
                    </div>
    
                    <div class="input-group">
                        <div class="form-floating">
                            <input type="password" name="password" class="form-control" id="passwInput" placeholder="*******">
                            <label for="floatingInput1">Password</label>
                        </div>
                    </div>
    
                    <input type="submit" id="loginButton" value="Sign in" class="d-button login-button">
                    <hr>
                    <div style="display: flex; justify-content: baseline;">
                        <a class="d-a register-prompt" onclick="showRegister()">No account? Register!</a>
                    </div>
                    
                </form>
    
                <form class="v-stack" id="regForm" style="display: none;">
                    <h1 class="login-heading">Register</h1>
                    <div class="input-group">
                        <div class="input-group-text">@</div>
                        <div class="form-floating">
                            <input minlength="5" name="username" required type="text" class="form-control" id="nameInput" placeholder="username">
                            <label for="floatingInput">Username</label>
                        </div>
                    </div>
                    <div class="input-group">
                        <div class="form-floating">
                            <input required name="email" type="email" class="form-control" id="mailInput" placeholder="username">
                            <label for="floatingInput">E-mail</label>
                        </div>
                    </div>
    
                    <div class="input-group">
                        <div class="form-floating">
                            <input minlength="8" name="password" type="password" class="form-control" id="passInput" placeholder="*******">
                            <label for="passInput1">Password</label>
                        </div>
                    </div>
    
                    <div class="input-group" style="margin-top: -7px;">
                        <div class="form-floating">
                            <input minlength="8" required name="password1" type="password" class="form-control" id="passInput1" placeholder="*******">
                            <label for="passInput1">Repeat Password</label>
                        </div>
                    </div>
    
                    <div class="form-check check-box">
                        <input style="width: auto;" requiredclass="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                        <label class="form-check-label" for="flexCheckDefault">
                        I agree to the <a href="#">terms and conditions</a>
                        </label>
                        <label style="padding-left: 2px; display: none;" for="flexCheckDefault" id="checkBoxErr" class="error1">Please check this box.</label>
                    </div>
    
                    <input type="submit" id="registerButton" value="Register" class="d-button login-button">
                    <hr>
                    <div style="display: flex; justify-content: baseline;">
                        <a class="d-a register-prompt" onclick="showLogin()">Have an account? Login!</a>
                    </div>
                </form>
            </div>
        </div>
        
        

        
        

        <script defer lang="ts">
            import { onMount } from 'svelte';
            import jQuery from 'jquery';
            import { page } from '$app/stores';

        
            function hasProblems() {
                if (jQuery('#flexCheckDefault').is(':checked')) {
                    jQuery("#checkBoxErr").css("display", "none");
                } else {
                    jQuery("#checkBoxErr").css("display", "block");
                }

                var isDisabled = false;
                if (document.querySelector(".error") != null) {
                    
                    for (const ele of document.querySelectorAll(".error")) {
                        if (ele.style.display !== "none") {
                            jQuery("#registerButton").prop("disabled", true);
                            isDisabled = true;
                            break;
                        }
                    }
                }
                else if (jQuery('#flexCheckDefault').is(':checked') == false) {
                    isDisabled = true;
                }

                if (isDisabled == false) {
                    jQuery("#registerButton").prop("disabled", false);
                }
                else if (isDisabled == true) {
                    jQuery("#registerButton").prop("disabled", true);
                }
            }

            
            
            

            function showLogin() {
                jQuery("#loginForm").show();
                jQuery("#regForm").hide();
            }

            function showRegister() {
                jQuery("#loginForm").hide();
                jQuery("#regForm").show();
            }

            

            // Do not refresh on submit, to use AJAX to send request
            export async function load({ params, url }) {
                let state = url.searchParams.get('state');
                return { state };
            }
            
            

            const register = $page.data.state;

            onMount(() => {
                jQuery('#regForm input').on("keyup", function() {
                    hasProblems();
                });
                setInterval(hasProblems, 500);
                jQuery("loginForm").submit(function(){
                    var username = jQuery('#logInput').text();
                    var password = jQuery('#passwInput').text();
                    jQuery.ajax('/api/v1/login.php', {
                        type: 'POST',  // http method
                        data: { username: username, password: password },  // TODO: encrypt pass
                        success: function (data, status, xhr) {
                            // TODO: fill in
                        },
                        error: function (jQueryXhr, textStatus, errorMessage) {
                            // TODO: fill in
                        }
                    });
                });
                jQuery(function(){
                    jQuery("#regForm").validate({
                        rules: {
                            password1: {
                                equalTo: "#passInput"
                            },
                            password: {
                                required: true
                            }
                        }
                    });
                    hasProblems();
                });
                if (register == 'reg') showRegister();
                jQuery(".login-form").submit(function(e) {
                    e.preventDefault();
                });

            });

            // TODO: make one for register button
        </script>