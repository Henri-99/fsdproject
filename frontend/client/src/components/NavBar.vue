<template>
	<nav class="navbar navbar-expand-lg bg-light sticky-top">
		<div class="container">
			<a class="navbar-brand" href="http://www.aifmrm.uct.ac.za/">
				<img src="src/assets/uct.png" alt="" width="50" height="50" class="logo">
				<img src="src/assets/logo.svg" alt="" width="100" height="50">
				<button class="navbar-toggler" type="button" data-bs-toggle="collapse"
					data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false"
					aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
			</a>
			<div class="collapse navbar-collapse" id="navbarNavDropdown">
				<ul class="navbar-nav">
					<li class="nav-item">
						<a class="nav-link active" aria-current="page" href="/Home">Home</a>
					</li>
					<li class="nav-item">
						<a class="nav-link active" aria-current="page" href="/charts">Charts</a>
					</li>
					<li class="nav-item">
						<a class="nav-link active" aria-current="page" href="/Indicies">Indicies</a>
					</li>
					<li class="nav-item">
						<a class="nav-link active" aria-current="page" href="/Shares">Shares</a>
					</li>
					<li class="nav-item">
						<a class="nav-link active" aria-current="page" href="/about">About</a>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</template>

<style>
.container-fluid {
	background-color: white;
}

.container {
	text-align: center;
}

.logo {
	margin-right: 10px;
}
</style>