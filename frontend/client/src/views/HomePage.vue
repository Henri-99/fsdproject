
<template>
	<!-- trying the slides -->
	<div>
		<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
			<div class="carousel-indicators img-fluid">
				<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
					aria-current="true" aria-label="Slide 1"></button>
				<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
					aria-label="Slide 2"></button>
				<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
					aria-label="Slide 3"></button>
			</div>
			<div class="carousel-inner">
				<div class="carousel-item active">
					<img src="../assets/Map.jpg" class="d-block w-100 img-fluid" alt="Responsive image">
					<div class="carousel-caption d-none d-md-block">
						<h5>Develop</h5>
						<p>Some representative placeholder content for the first slide.</p>
					</div>
				</div>
				<div class="carousel-item">
					<img src="../assets/Plant.jpg" class="d-block w-100 img-fluid" alt="Responsive image">
					<div class="carousel-caption d-none d-md-block">
						<h5>Shape</h5>
						<p>Some representative placeholder content for the second slide.</p>
					</div>
				</div>
				<div class="carousel-item">
					<img src="../assets/advance.jpg" class="d-block w-100 img-fluid"
						alt="Responsive image">
					<div class="carousel-caption d-none d-md-block">
						<h5>Advance</h5>
						<p>Some representative placeholder content for the third slide.</p>
					</div>
				</div>
			</div>
			<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
				data-bs-slide="prev">
				<span class="carousel-control-prev-icon" aria-hidden="true"></span>
				<span class="visually-hidden">Previous</span>
			</button>
			<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
				data-bs-slide="next">
				<span class="carousel-control-next-icon" aria-hidden="true"></span>
				<span class="visually-hidden">Next</span>
			</button>
		</div>
	</div>




	<!-- Home page jumpotron -->
	<p></p>
	<div class="p-5 mb-4 bg-light rounded-3 container">
		<div class="container-fluid py-5">
			<h1 class="display-5 fw-bold">Develop, Share & Advance</h1>
			<p class="col-md-8 fs-4"></p>

			<!-- graph and sentence 1 -->
			<div class="row">
				<div class="col-6">
					<img class="image" src="https://static.thenounproject.com/png/2196096-200.png" alt="Topic 1">
				</div>
				<div class="col-6 jumpo-para">
					<p>AIFMRM provides an equity risk service to the South African financial services sector, this
						webpage will
						include rich statistics and analysis on all the indices listed on the JSE's limited equity
						market for ordinary shares.
					</p>
				</div>
			</div>

			<!-- graph and sentence 2 -->
			<div class="row">
				<div class="col-6 jumpo-para2">
					<p>The following is the list of the most important risk statistics using modified CAPM and Beta of
						each share.
					<ol type="i">
						<li>All Share (J203);</li>
						<li>Top 40 (J200);</li>
						<li>Financials and Industrials (J250);</li>
						<li>Industrials (J257); and</li>
						<li>Resources (J258) indices</li>
					</ol>
					</p>
				</div>
				<div class="col-6">
					<img class="image2" src="https://static.thenounproject.com/png/2196096-200.png" alt="Topic 1">
				</div>
			</div>
			<!-- <button class="btn btn-info btn-lg buttons" type="button">Example button</button> -->
		</div>
	</div>

<!-- Footer -->
<footer>
	<router-link :to="{ name: 'HomePage' }" class="footerLinks">
			Home
	</router-link>
	<router-link :to="{ name: 'FAQPage' }" class="footerLinks">
			FAQs
	</router-link>
	<router-link :to="{ name: 'PingTest' }" class="footerLinks">
			Index Constituents
	</router-link>
	<router-link :to="{ name: 'TimeSeries' }" class="footerLinks">
			Time Series
	</router-link>
	<router-link :to="{ name: 'StatsPage' }" class="footerLinks">
			Statistics
	</router-link>
	<p class="footerText">Copyright © 2022 Faculty of Commerce - University of Cape Town</p>
</footer>


</template>

<style>
h1 {
	text-align: center;
	color: #1D70B7;
}

.image {
	margin-left: 10%;
}

.jumpo-para {
	border-right: 5cm;
	margin-top: 5%;
}

.jumpo-para2 {
	margin-top: 10%;
}

.image2 {
	margin-left: 25%;
	margin-top: 20%;
}

.buttons {
	background-color: #1D70B7;
	color: white;
	margin-top: 5%;
}

footer {
	background-color: #1D70B7;
	padding: 0.1%;
	padding-top: 0.9%;
}

.footerLinks {
	padding: 5%;
	padding-bottom: 3%;
	padding-top: 2%;
}

.footerText {
	margin-top: 0.5%;
	color: white;
	font-size: medium;
	text-align: center;
}

/* p {
  color: #1D1D1B;
} */



/* Slides Styling */
</style>
