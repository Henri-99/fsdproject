
<template>
	<header>
		<nav class="navbar navbar-expand-lg bg-light sticky-top">
			<div class="container">
				<img src="./assets/uct.png" alt=""  height="80" class="logo">
				<img src="./assets/logo.svg" alt="" height="80" class="logo">
				<button class="navbar-toggler" type="button" data-bs-toggle="collapse"
					data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false"
					aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNavDropdown">
					<ul class="navbar-nav">
						<li class="nav-item  btn btn-primary">
							<router-link :to="{ name: 'HomePage' }">
								Home
							</router-link>
						</li>

						<li class="nav-item  btn btn-primary">
							<router-link :to="{ name: 'PingTest' }">
								Index Constituents
							</router-link>
						</li>

						<li class="nav-item  btn btn-primary">
							<router-link :to="{ name: 'TimeSeries' }">
								Time Series
							</router-link>
						</li>

						<li class="nav-item  btn btn-primary">
							<router-link :to="{ name: 'StatsPage' }">
								Statistics
							</router-link>
						</li>
						<li class="nav-item  btn btn-primary">
							<router-link :to="{ name: 'PortfolioBuilder' }">
								Portfolio Builder
							</router-link>
						</li>

						<li class="nav-item  btn btn-primary">
							<router-link :to="{ name: 'FAQPage' }">
								FAQs
							</router-link>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	</header>

	<body>
		<div id="app" class="body">


			<router-view />

		</div>
	</body>

</template>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}

.body {
	margin-top: 1rem;
}

.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-column-gap: 1rem;
  max-width: 960px;
  margin: 0 auto;
}

.logo{
	padding-right: 3%;
}
.navbar{
	--bs-navbar-padding-y: 1rem;
}

.nav-item{
    color: #000000;
    text-decoration: none;
	margin-left: 10px;
	font-size: 20px;
}

a:link {
  color: white;
  background-color: transparent;
  text-decoration: none;
}

a:visited {
  color: white;
  background-color: transparent;
  text-decoration: none;
}

a:hover {
  color: white;
  background-color: transparent;
  text-decoration: underline;
}

.btn-primary{
	background-color: #1D70B7;
	border-color: #1a62a1;
}


/* Colours: grey:  #1D1D1B
			blue:  #1D70B7 */
</style>
