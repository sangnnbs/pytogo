<!-- This is Basic knowledge of Svelte - FrontEnd Framework 
There is tutorial of Svelte online: https://svelte.dev/tutorial/

-->
<!-- Value Svelte in HTML:   $          => value prefix multi-stores 
                             bind:value => value bind input
                                       
-->


<!-- Block Svelte in HTML:   # => block open Tag 
                             / => block close Tag
                             : => block continue tag
                                       
-->

{#each lists as l (l.id)}
    HTML {l.dataInLists}
{/each}

{#if conditions}
    HTML
{:else if conditions}
    HTML 
{:else}
    HTML 
{/if}

{#await someFunc}
    HTML
{:then someVariable}
    HTML {someVariable}
{:catch error}
    HTML {error.message}
{/await}

## Event Modifiers - Check document: https://svelte.dev/tutorial/event-modifiers

listEvent = {
    preventDefault,
    stopPropagation,
    passive,
    nonpassive,
    capture,
    once,
    self,
    trusted
}