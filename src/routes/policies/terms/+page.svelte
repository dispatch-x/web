<style lang="scss">
    @import '../policies';
</style>
<script lang="ts">
    import Navbar from '../../Navbar.svelte';
    import Footer from '../../Footer.svelte';
</script>
<Navbar />
<div class="content">
    <h2 id="dispatchx-terms-of-service">Dispatch Terms of Service</h2>
    <p><em>This is not a legal document. This is a summarization of what it actually is. See the real deal <a href="/policies/terms/legal">here</a>.</em></p>
    <p>If you use Dispatch, you agree to the terms of service stated below, and must follow them.</p>
    <h3 id="1-expletives-and-harassment">1 - Expletives and Harassment</h3>
    <p>This is not tolerated on Dispatch, and is governed through a secure profanity filter. Anything rude will be returned with a <code>422 Unprocessable Entity</code> HTTP error code. If you engage in such activity, you run the risk of a permanent ban.</p>
    <h3 id="2-attempted-cracking">2 - Attempted Cracking</h3>
    <p>Attempted cracking is not permitted. We encrypt all user data, and protect against SQL injection and JS injection attacks. All transfer is conducted, between two HTTPS sites. Whilst it is allowed and encouraged to set up your own Dispatchx client, for example <code>werdl/pydispatchx</code>, you must credit this repository and you cannot attempt to crack the database.</p>
    <h3 id="3-general-rules">3 - General Rules</h3>
    <p>Please do not say anything on this site you would not say in person! Please remember that behind every monitor there is a human.</p>
    <br>
</div>
<Footer />