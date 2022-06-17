<script setup>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
import charts from './components/charts.vue';

</script>

<template>
	

	<header>
		<NavBar />
		<table class="center">
			<tr>
				<td><img alt="UCT logo" class="logo" src="./assets/uct_logo.png" height="200" /></td>
				<td><img alt="AIFMRM logo" class="logo" src="./assets/logo.svg" width="400" height="250" /></td>
			</tr>
		</table>

		<div class="wrapper">
			<HelloWorld msg="Welcome to the FSD Dashboard!" />
		</div>


	</header>

	<main>

		 <div class="p-5 mb-4 bg-light rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">Welcome to the FSD dashboard</h1>
        <p class="col-md-8 fs-4">
				<b>Backlog</b>
				<li>Styling</li>
				<s><li>Navigation bar</li></s>
				<li>Flask API</li>
				<li>User forms</li>
				<li>Info about AIFMRM</li>
				<li>Indices</li>
				<li>Shares</li>
				<li>Graphs</li>
				<li>FAQ</li></p>
        <button class="btn btn-primary btn-lg" type="button"><a href="https://www.fbcironton.org/hp_wordpress/wp-content/uploads/2019/12/085188115_prevstill.jpeg">Click to see a surprise</a></button>
      </div>
    </div>
		<div class="backlog">
			<p>
				<b>Backlog</b>
				<li>Styling</li>
				<li>Navigation bar</li>
				<li>Flask API</li>
				<li>User forms</li>
				<li>Info about AIFMRM</li>
				<li>Indices</li>
				<li>Shares</li>
				<li>Graphs</li>
				<li>FAQ</li>
			</p>

		</div>
	</main>
</template>

<style>

.center {
  margin-left: auto;
  margin-right: auto;
}

header {
	text-align : center;
}

.wrapper {
	font-family: Arial, Helvetica, sans-serif;
	
}

.backlog {
	margin-left: 60pt;
	font-family: Arial, Helvetica, sans-serif;
}


/* Colours: grey:  #1D1D1B
			blue:  #1D70B7 */
</style>
