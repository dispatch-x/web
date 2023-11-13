<style lang="scss">
    @import '../policies';
</style>
<script lang="ts">
    import Navbar from '../../Navbar.svelte';
</script>
<Navbar />
<div class="content">
    <h2 id="dispatch-technical-policy">Dispatch Technical Policy</h2>
    <p>This document details how Dispatchx works under the hood, and how user data is protected.</p>
    <h3 id="what-is-encrypted-hashed">What is encrypted/hashed</h3>
    <p>Things that are encrypted or hashed are listed in the privacy policy.</p>
    <h3 id="how-encryption-works">How encryption works</h3>
    <p>We use the Python <code>cryptography.fernet</code> module for encryption of user data. It is common for storing small amounts of data. The keys are securely stored in an encrypted DB. It leverages several common cryptographic primitives, specifically <code>AES-128</code> in <code>CBC</code> mode using <code>PKCS7</code> padding, and <code>HMAC</code> and <code>SHA256</code> for authentication. It relies on <code>os.urandom</code>, and our server runs on <code>Ubuntu 22.04</code>, at last check using kernel version <code>6.2.0</code>.</p>
    <h3 id="how-hashing-works">How hashing works</h3>
    <p>We use the Python module <code>bcrypt</code> to hash passwords. <code>bcrypt</code> is among the most secure password hashing solutions, as it uses salts, is intentionally slow (making attacks computationally expensive). Behind the scenes, it uses <code>Blowfish</code> for the hashing and <code>KDF</code> functions. For the work factor, we use 12, a balance between security and performance (and the industry standard).</p>
</div>
