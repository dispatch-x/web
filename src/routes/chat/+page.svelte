<style lang="scss">
    @import '../main';
    * {
        font-family: 'Outfit', $font-sans-serif;
    }
    .header {
        padding: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        // border-bottom: 1px solid lightgray;
        .add-button {
            position: absolute;
            right: 0;
            border: none;
            background: transparent;
            color: $link-color;
            padding: 0 1rem;
            height: 100%;
            
        }
        strong, .add-button {
            font-size: 16pt;
        }
    }
    main {
        .chat {
            padding: .75rem;
            display: flex;
            gap: 10px;
            align-items: center;
            justify-content: baseline;
            cursor: pointer;
            transition: 0.2s;
            .chat-img {
                img {
                    border-radius: 50%;
                    aspect-ratio: 1 / 1;
                    height: 48px;
                }
            }
            .chat-content {
                display: flex;
                flex-direction: column;
            }
            &:hover {
                background: $gray-200;
            }
        }
        hr {
            margin: 0!important;
        }
    }
</style>
<script>
    // TODO: modify #each, etc.
    let chats = [
        {
            roomName: "silly billy fam",
            recentMessage: "George: hello",
            image: "/misc/chat.webp",
            recentTime: "18:09",
            notBadge: "2"
        },
        {
            roomName: "",
            recentMessage: "",
            image: "/misc/chat.webp",
            recentTime: "",
            notBadge: "2"
        },
        
    ];
</script>
<header class="header bg-body-tertiary">
    <strong>Rooms</strong>
    <button class="add-button"><i class="fa-solid fa-plus"></i></button>
</header>
<main>
    {#each chats as chat}
        <div class="chat">
            <div class="chat-img">
                <img src="/misc/chat.webp" alt="Logo of {chat}" class="lazyload">
            </div>
            <div class="chat-content">
                <strong>{chat}</strong>
                <span class="text-muted">Lorenzo: GIF</span>
            </div>
        </div>
        <hr>
    {/each}
</main>
<footer>

</footer>