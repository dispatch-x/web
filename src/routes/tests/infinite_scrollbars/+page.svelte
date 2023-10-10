<script>
    import jQuery from 'jquery';
    import { onMount } from 'svelte';
    
    let hi;
    let yes = false;
    let colors = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99];
    
    function randomize(searchEles) {
        if (yes !== false) {
            for (let i = 0; i < searchEles.length; i++) {
                jQuery(".no-"+i.toString()).animate({
                    scrollLeft: (Math.floor(Math.random() * (jQuery(".no-"+i).width())-50)).toString()+"px"
                }, 5000-(parseInt(document.getElementById("range").value)));
            }
        }
        else {
            clearInterval(hi);
        }
    }
    function yesno(searchEles) {
        if (yes !== false) {
            hi = setInterval(() => { randomize(searchEles); }, 100);
        }
    }
    onMount(() => {
        var searchEles = document.querySelector(".cont").children;
        jQuery("#random").on("click", () => {
            yes = true;
            randomize(searchEles);
            yes = false;
        });
        setInterval(() => { yesno(searchEles); }, 500);
    });
</script>
<style lang="scss">
    .hi {
        width: 100%;
        height: 18px;
        overflow: auto;
    }
    .cont {
        overflow: auto;
        width: 100%;
    }
    .bye {
        width: 200%;
    }
    .random {
        position: fixed;
        top: 1rem;
        left: 1rem;
        display: flex;
        gap: .5rem;
        button {
            border-radius: 5px;
        }
        div {
            background: white;
            border-radius: .5rem;
            padding: .5rem;
            width: 4rem;
            transition: 0.4s;
            overflow: hidden;
            white-space: nowrap;
            &:hover {
                width: auto;
            }
            * {
                cursor: pointer;
            }
        }
    }
</style>
<div class="random">
    <button id="random">Randomize</button>
    <div>
        <input bind:checked={yes} type="checkbox" id="randomi">
        <label for="randomi" >Randomize again and again and again and again!!!!!</label>
    </div>
    <div>
        <input type="range" id="range" min="0" max="5000" value="2500">
        <label for="range">Speed</label>
    </div>
</div>

<div class="cont">
    {#each colors as color}
        <div class="hi no-{color}"><div class="bye"></div></div>
    {/each}
</div>
