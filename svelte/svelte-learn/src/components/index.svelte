<script>
import Category from "./partials/blocks/category.svelte";

import HeroSlider from "./partials/blocks/hero-slider.svelte";

import Navigation from "./partials/blocks/navigation.svelte";


import Footer from "./partials/Footer.svelte";
import Header from "./partials/Header.svelte";

</script>

<Header></Header>

<Navigation></Navigation>

<HeroSlider></HeroSlider>

<Category></Category>

<section class="products section bg-gray">
	<div class="container">
		<div class="row">
			<div class="title text-center">
				<h2>Trendy Products</h2>
			</div>
		</div>
		<div class="row">
			@@include('blocks/product.htm')
		</div>
	</div>
</section>

<Footer></Footer>