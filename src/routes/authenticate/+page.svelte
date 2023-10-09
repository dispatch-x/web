<img class="background" src="/assets/img/backgrounds/bg-1.jpg">
        <div class="login-wrapper-wrapper">
            <div class="login-wrapper">
                <img class="logo" src="/assets/img/logo/android-chrome-192x192.png">
                
                
                
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
            const jq = window.$;

        
            function hasProblems() {
                if (jq('#flexCheckDefault').is(':checked')) {
                    jq("#checkBoxErr").css("display", "none");
                } else {
                    jq("#checkBoxErr").css("display", "block");
                }

                var isDisabled = false;
                if (document.querySelector(".error") != null) {
                    
                    for (const ele of document.querySelectorAll(".error")) {
                        if (ele.style.display !== "none") {
                            jq("#registerButton").prop("disabled", true);
                            isDisabled = true;
                            break;
                        }
                    }
                }
                else if (jq('#flexCheckDefault').is(':checked') == false) {
                    isDisabled = true;
                }

                if (isDisabled == false) {
                    jq("#registerButton").prop("disabled", false);
                }
                else if (isDisabled == true) {
                    jq("#registerButton").prop("disabled", true);
                }
            }

            
            
            

            function showLogin() {
                jq("#loginForm").show();
                jq("#regForm").hide();
            }

            function showRegister() {
                jq("#loginForm").hide();
                jq("#regForm").show();
            }

            

            // Do not refresh on submit, to use AJAX to send request
            

            const urlParams = new URLSearchParams(window.location.search);
            const register = urlParams.get('state');

            onMount(() => {
                jq('#regForm input').on("keyup", function() {
                    hasProblems();
                });
                setInterval(hasProblems, 500);
                jq("loginForm").submit(function(){
                    var username = jq('#logInput').text();
                    var password = jq('#passwInput').text();
                    jq.ajax('/api/v1/login.php', {
                        type: 'POST',  // http method
                        data: { username: username, password: password },  // TODO: encrypt pass
                        success: function (data, status, xhr) {
                            // TODO: fill in
                        },
                        error: function (jqXhr, textStatus, errorMessage) {
                            // TODO: fill in
                        }
                    });
                });
                jq(function(){
                    jq("#regForm").validate({
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
                jq(".login-form").submit(function(e) {
                    e.preventDefault();
                });

            });

            // TODO: make one for register button
        </script>