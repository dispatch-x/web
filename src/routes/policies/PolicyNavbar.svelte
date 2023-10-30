
<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    const navLinks = [
      { text: 'Technica Policy', href: '/policies/technical' },
      { text: 'Privacy Policy', href: '/policies/privacy' },
      { text: 'Terms of Service', href: '/policies/terms' },
    ];
    let isRoot = false; // if we are in the root of the project
    let style_isRoot="margin: 7vh";
    if (!isRoot) {
        style_isRoot="";
    }
    $: {
      isRoot = $page.url.pathname === '/' || $page.url.pathname === '';
    }
  
    onMount(() => {
      const unsubscribe = page.subscribe(($page) => {
        isRoot = $page.url.pathname === '/' || $page.url.pathname === '';
        style_isRoot="margin-bottom: 7vh";
        if (!isRoot) {
            style_isRoot="";
        }
      });
  
      return () => {
        unsubscribe();
      };
    });

</script>
<style lang="scss">
    div.policynav {
        background-color: #333;
        text-align: center;
        transition: background-color 0.3s ease; /* Smooth transition effect */
    }
    div.policynav a {
        color: white;
        text-decoration: none;
        padding: 16px 16px; /* Adjusted padding to extend to top and bottom */
        display: inline-block;
    }
    
    div.policynav a:hover {
        background-color: #222; /* Darker grey on hover for the entire navbar */
    }
    div.margin_bottom {
        margin-bottom: 7vh;
    }
    </style>
<div class="policynav" class:margin_bottom={isRoot}>
{#if !isRoot}
    <a href="/">Home</a>
{/if}

{#each navLinks as { text, href }}
    <a href={href}>{text}</a>
{/each}
</div>
