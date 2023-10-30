<style lang="scss">
    @import '../policies';
</style>
<script lang="ts">
    import PolicyNavbar from "../PolicyNavbar.svelte";
</script>
<PolicyNavbar />
<div class="content">
    <h2 id="dispatchx-privacy-policy">Dispatchx Privacy Policy</h2>
    <p>This piece of software is licensed under the Mozilla Public License 2.0, a version of which is kept in <code>LICENSE</code>.</p>
    <h3 id="1-user-data">1 - User Data</h3>
    <p>We do not store any identifying details of users that are not provided to us. We also do not access any user details, or glean any data from the <code>messages</code> table.</p>
    <h3 id="2-chatroom-data">2 - Chatroom Data</h3>
    <p>Each chatroom has its own row in <code>rooms</code>, containing the room uuid, used so that multiple rooms can have the same alias, the alias (nickname) of a room (encrypted), the list of users in the room (encrypted), and the creator of the room (encrypted).</p>
    <h3 id="3-message-data">3 - Message Data</h3>
    <p>Messages are stored with a room uuid in the <code>messages</code> table. The data stored contains the message uuid, the room uuid, the sender (encrypted), the content (encrypted), and the UTC timestamp of when it was sent. Messages have a uuid, but the are not currently in use, rather there for future purposes such as message deletion.</p>
</div>
