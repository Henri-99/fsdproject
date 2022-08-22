<template>

	<!-- The FAQ Page -->
	<!-- The FAQ drop down text boxes -->
	<p></p>
	<h3>Frequently Asked Questions (FAQ)</h3>
	<p></p>
	<div class="container">
		<div class="accordion">
			<div class="accordion-item">
				<div class="card-header" id="headingSix">
					<h5 class="mb-0">
						<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSix" aria-expanded="true" aria-controls="collapseSix">
							How to measure a portfolio's perfomance?
						</button>
					</h5>
				</div>

				<div id="collapseSix" class="collapse show" aria-labelledby="headingSix" data-parent="#accordion">
					<div class="card-body">
						In the past, many managers have compared their funds on the basis of returns alone.
						Performance figures that are unadjusted for risk indicate how much money the portfolio has
						earned but provide no information about the risks that were taken.
						Managers may argue that it is profit that clients are concerned with and find it difficult to
						convince clients that their
						portfolios yield lower returns than their competitors simply because they are exposed to lower
						risks.
						But managers who take on unnecessarily high-risk portfolios to gain a competitive edge on return
						are foolish
						and will be managers no more when the market turns bearish. Merit should always go to the
						managers
						who have achieved the highest risk-adjusted returns even if their unadjusted returns are lower.
					</div>
				</div>
			</div>
			<div class="accordion-item">
				<div class="card-header" id="headingSeven">
					<h5 class="mb-0">
						<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSeven" aria-expanded="false" aria-controls="collapseSeven">
							How is risk calculated?
						</button>
					</h5>
				</div>
				<div id="collapseSeven" class="collapse" aria-labelledby="headingSeven" data-parent="#accordion">
					<div class="card-body">
						By now it should be clear that, for portfolios, beta is the most important component of risk
						(since market risk is the dominant risk component for diversified portfolios). The beta of a
						portfolio tells us how sensitive it is to market movements. Calculating a portfolio’s beta is
						straightforward: simply look up the individual betas of the constituent shares and weight each
						one by the proportion of the fund that is invested in that share. The sum of these weighted
						values will yield your portfolio’s beta (to calculate the actual amount of market risk that a
						portfolio has.



						The measurement of the unique risk of a portfolio is slightly more intricate. Naturally, if a
						portfolio is the market index or something very close to it, the unique risk of the portfolio
						will be virtually zero.



						However, if a portfolio is not diversified, one may need some data on the recent history of the
						portfolio’s performance. Alternatively, if a portfolio is reasonably diversified, one may
						calculate the portfolio’s unique risk from the unique risk figures of the constituent shares,
						analogous to the method employed in the worked example in Section 6. If a portfolio is well
						diversified, this approach gives a good estimate of its unique risk. However, if many of the
						shares in a portfolio are clustered in one industry, then the true unique risk will be slightly
						higher than calculated. Once the two risk components of a portfolio have been quantified, these
						may be compared, for instance, your target levels. If either of the risk components is off
						target, the remedy is clear.



						Traditionally, the approaches to portfolio management have included: restricting selection
						choices to

						an eligible list of large companies; specifying a minimum yield level; restricting the
						proportion in a single share or sector; and even authorising every deal that is made. This can
						impose unnecessary constraints that fail to control the risks. The modern way to manage
						portfolios is to measure beta and unique risk on an ongoing basis and to track actual levels to
						target levels
					</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Definitions Boxes -->
	<p></p>
	<h3>Definitions</h3>
	<p></p>
	<div class="container">
		<div class="accordion">

			<div class="accordion-item">
				<div class="card-header" id="headingTwo">
					<h5 class="mb-0">
						<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
							Beta
						</button>
					</h5>
				</div>
				<div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
					<div class="card-body">
						This is the sensitivity of the respective index level to changes in the market proxyx, where x
						=J203, J200, J250, J257 or J258. A beta greater than 1 implies that the index will tend to move
						more in percentage terms than the market proxy and vice versa.
						Monthly excess returns (actual returns in excess of the risk-free return) are computed for each
						share as well as for each of the proxy indices. Risk-free rates of return are computed from the
						JSE’s nominal swap yield curve, by rolling an overnight investment
						over the respective return period. If, however, a share has not been traded at a respective
						month-end, the returns are computed between last and previous trade dates - this is the thin
						trading adjustment. If one were to plot these points with the index’s returns
						on the horizontal axis and the share’s returns on the vertical axis (as shown below), beta would
						be the slope of the line that best fits these points.
					</div>
				</div>
			</div>
			<div class="accordion-item">
				<div class="card-header" id="headingThree">
					<h5 class="mb-0">
						<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
							Unique and specific risk
						</button>
					</h5>
				</div>
				<div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
					<div class="card-body">
						Unsystematic risk or idiosyncratic risk. Specific company risk that can be eliminated through
						diversification, meaning the dangers that are unique to a single company or industry. However,
						these risks do not only occur one firm at a time. For example, a poor manager might pose a
						specific risk to a single company's stock price.
					</div>
				</div>
			</div>
			<div class="accordion-item">
				<div class="card-header" id="headingFour">
					<h5 class="mb-0">
						<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
							Market or systamatic risk
						</button>
					</h5>
				</div>
				<div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordion">
					<div class="card-body">
						Market risk represents economy-wide factors that are out of your control, like interest rates,
						government spending, inflation, etc.
					</div>
				</div>
			</div>
			<div class="accordion-item">
				<div class="card-header" id="headingTwo">
					<h5 class="mb-0">
						<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
							Systematic versus specific risk
						</button>
					</h5>
				</div>
				<div id="collapseFive" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
					<div class="card-body endpage">
						specific risk, or unsystematic risk, only affects an industry or particular company. On the
						other hand, systemic risk also called market risk affects the market as a whole.
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- The Formulas drop down text boxes -->
	<div class="endPage"></div>

</template>

<style>
h3 {
	text-align: center;
	color: #1D70B7;
}

.endPage {
	margin-bottom: 10%;
}

.btn {
	color: #1D1D1B;
}

.card-body {
	padding: 1rem 1rem 1rem 1.5rem;
	text-align: left;
	font-size: 0.9rem;
}
</style>
