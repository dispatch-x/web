<style>
  .navbar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  font-family: "Outfit", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
  background: transparent;
  background: rgba(0, 0, 0, 0.03);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  z-index: 1;
}
.navbar button.d-button {
  width: 75%;
}
.navbar button.d-button-secondary {
  width: 25%;
}
a.d-button, a.d-button-secondary {
  text-align: center;
  text-decoration: none;
}

.d-button {
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #0070e0;
  background: #007FFF;
  color: white;
  font-family: "Outfit", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  cursor: pointer;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  transition: 0.2s;
  font-weight: 200;
}
.d-button:hover {
  background: #0079f1;
}
.d-button:active {
  box-shadow: none;
  background: #0070e0;
}

.d-button-secondary {
  padding: 10px;
  border-radius: 10px;
  border: 2px solid #007FFF;
  color: black;
  background: white;
  font-family: "Outfit", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  cursor: pointer;
  box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  transition: 0.2s;
  font-weight: 200;
}
.d-button-secondary:hover {
  background: #f8f9fa;
}
.d-button-secondary:active {
  box-shadow: none;
}
@media (min-width: 992px) {
  .navbar .container-fluid .collapse form.d-flex button, .navbar .container-sm .collapse form.d-flex button, .navbar .container-md .collapse form.d-flex button, .navbar .container-lg .collapse form.d-flex button, .navbar .container-xl .collapse form.d-flex button, .navbar .container-xxl .collapse form.d-flex button {
    width: auto !important;
  }
}
</style>
<nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="/"><img alt="Logo" style="height: 48px;" src="/icons/android-chrome-192x192.png"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
        <form class="d-flex login-prompt" role="login">
          <a href="/authenticate.html?state=reg" class="d-button" style="margin-right: 0.5rem; width: 75%;">Sign Up</a>
          <a href="/authenticate.html" class="d-button-secondary" style="width: 25%;">Sign In</a>
        </form>
      </div>
    </div>
</nav>