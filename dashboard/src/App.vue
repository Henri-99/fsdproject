<script setup>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
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
