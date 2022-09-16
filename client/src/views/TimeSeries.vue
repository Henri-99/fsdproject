<template>
	<div class="flex-container" style="margin: 2rem">
		<v-select class="tickerbox" v-model="stock"
			:options="['4SI : 4Sight Holdings Ltd', 'ABG : Absa Group Limited', 'ACL : ArcelorMittal SA Limited', 'ACS : Acsion Limited', 'ACT : AfroCentric Inv Corp Ltd', 'ACZ : Arden Capital Limited', 'ADH : ADvTECH Ltd', 'ADI : Adapt IT Holdings Ltd', 'ADR : Adcorp Holdings Limited', 'ADW : African Dawn Capital Ltd', 'AEE : African Equity Emp Inv Ltd', 'AEG : Aveng Group Limited', 'AEL : Allied Electronics Corp A', 'AFE : AECI Limited', 'AFH : Alexander Forbes Grp Hldgs', 'AFT : Afrimat Limited', 'AGL : Anglo American plc', 'AHA : Arrowhead Prop Ltd A', 'AHB : Arrowhead Prop Ltd B', 'AHL : AH-Vest Limited', 'AIL : African Rainbow Cap Inv', 'AIP : Adcock Ingram Hldgs Ltd', 'ALH : Alaris Holdings Ltd', 'AME : African Media Ent Ltd', 'AMS : Anglo American Plat Ltd', 'ANG : Anglogold Ashanti Ltd', 'ANH : Anheuser-Busch InBev SA NV', 'AON : African & Over Ent Ltd -N', 'AOO : African & Over Ent Ltd', 'APF : Accelerate Prop Fund Ltd', 'APH : Alphamin Resources Corp', 'APN : Aspen Pharmacare Hldgs Ltd', 'ARA : Astoria Investments Ltd', 'ARH : ARB Holdings Limited', 'ARI : African Rainbow Min Ltd', 'ARL : Astral Foods Ltd', 'ART : Argent Industrial Ltd', 'ASC : Ascendis Health Ltd', 'ATI : Afristrat Inv Hldgs Ltd', 'ATT : Attacq Limited', 'AVI : AVI Ltd', 'AVL : Advanced Health Ltd', 'AVV : Alviva Holdings Ltd', 'AYO : Ayo Tech Solutions Ltd', 'BAT : Brait SE', 'BAU : Bauba Resources Limited', 'BAW : Barloworld Ltd', 'BCF : Bowler Metcalf Ltd', 'BEL : Bell Equipment Ltd', 'BHP : BHP Group Plc', 'BID : BID Corporation Ltd', 'BIK : Brikor Ltd', 'BLU : Blue Label Telecoms Ltd', 'BRN : Brimstone Inv Corp Ltd-N', 'BRT : Brimstone Inv Corp Ltd', 'BSR : Basil Read Holdings Ltd', 'BTI : British American Tob plc', 'BUC : Buffalo Coal Corp', 'BVT : Bidvest Ltd', 'BWN : Balwin Properties Ltd', 'BYI : Bytes Technology Group', 'CAC : Cafca Limited', 'CAT : Caxton CTP Publish Print', 'CCO : Capital&Counties Prop plc', 'CFR : Compagnie Fin Richemont', 'CGN : Cognition Holdings Ltd', 'CGR : Calgro M3 Hldgs Ltd', 'CHP : Choppies Enterprises Ltd', 'CIL : Cons Infrastructure Grp Ltd', 'CKS : Crookes Brothers Ltd', 'CLH : City Lodge Hotels Ltd', 'CLI : Clientele Ltd', 'CLS : Clicks Group Ltd', 'CMH : Combined Motor Hldgs Ltd', 'CML : Coronation Fund Mngrs Ld', 'CMO : Chrometco Ltd', 'CND : Conduit Capital Ltd', 'COH : Curro Holdings Limited', 'COM : Comair Limited', 'CPI : Capitec Bank Hldgs Ltd', 'CRP : Capital & Regional Plc', 'CSB : Cashbuild Ltd', 'CSG : CSG Holdings Ltd', 'CTA : CAPITAL APPRECIATION LTD', 'CTK : Cartrack Holdings Ltd', 'CVW : Castleview Prop Fund Ltd', 'DCP : Dis-Chem Pharmacies Ltd', 'DGH : Distell Group Hldgs Ltd', 'DIA : Dipula Income Fund A', 'DIB : Dipula Income Fund B', 'DLT : Delta Property Fund Ltd', 'DNB : Deneb Investments Ltd', 'DRD : DRD Gold Ltd', 'DSY : Discovery Ltd', 'DTC : Datatec Ltd', 'EEL : Efora Energy Limited', 'ELI : Ellies Holdings Ltd', 'EMH : E Media Holdings Ltd', 'EMI : Emira Property Fund Ltd', 'EMN : E Media Holdings Ltd -N-', 'ENX : enX Group LImited', 'EOH : EOH Holdings Ltd', 'EPE : EPE Capital Partners Ltd', 'EPP : EPP N.V.', 'EPS : Eastern Platinum Ltd', 'EQU : Equites Prop Fund Ltd', 'ERN : Erin Energy Corporation', 'ETO : Etion Limited', 'EUZ : Europa Metals Limited', 'EXP : Exemplar REITail Ltd', 'EXX : Exxaro Resources Ltd', 'FBR : Famous Brands Ltd', 'FDP : Freedom Prop Fund Ltd', 'FFA : Fortress REIT Ltd A', 'FFB : Fortress REIT Ltd B', 'FGL : Finbond Group Ltd', 'FSE : Firestone Energy Limited', 'FSR : Firstrand Ltd', 'FVT : Fairvest Property Hldgs', 'GFI : Gold Fields Ltd', 'GLI : Go Life International Ld', 'GLN : Glencore plc', 'GML : Gemfields Group Limited', 'GND : Grindrod Ltd', 'GPL : Grand Parade Inv Ltd', 'GRT : Growthpoint Prop Ltd', 'GSH : Grindrod Shipping Hldg Ltd', 'GTC : Globe Trade Centre S.A.', 'HAR : Harmony GM Co Ltd', 'HCI : Hosken Cons Inv Ltd', 'HDC : Hudaco Industries Ltd', 'HET : Heriot REIT Limited', 'HIL : Homechoice Int plc', 'HLM : Hulamin Ltd', 'HMN : Hammerson plc', 'HPR : Hosken Pax Log and Rail', 'HUG : Huge Group Ltd', 'HUL : Hulisani Limited', 'HWA : Hwange Colliery Ltd', 'HYP : Hyprop Inv Ltd', 'IAP : Irongate Group', 'ILE : Imbalie Beauty Limited', 'ILU : Indluplace Properties Ltd', 'IMP : Impala Platinum Hlgs Ltd', 'INL : Investec Ltd', 'INP : Investec plc', 'IPF : Investec Property Fund Ltd', 'IPL : Imperial Logistics Ltd ', 'ISA : ISA Holdings Limited', 'ISB : Insimbi Ind Hldgs Ltd', 'ITE : Italtile Ltd', 'IVT : Invicta Holdings Ltd', 'JBL : Jubilee Metals Group plc', 'JSC : Jasco Electron Hldgs Ltd', 'JSE : JSE Ltd', 'KAL : Kaap Agri Limited', 'KAP : KAP Industrial Hldgs Ltd', 'KBO : Kibo Energy plc', 'KDV : Kaydav Group Ltd', 'KIO : Kumba Iron Ore Ltd', 'KP2 : Kore Potash plc', 'KST : PSG Konsult Limited', 'L2D : Liberty Two Degrees LTD', 'L4L : Long 4 Life Limited', 'LBH : Liberty Holdings Ltd', 'LBR : Libstar Holdings Ltd', 'LEW : Lewis Group Ltd', 'LHC : Life Healthc Grp Hldgs Ltd', 'LNF : London Fin Inv Group plc', 'LTE : Lighthouse Capital Ltd', 'LUX : Luxe Holdings Limited', 'MCG : MultiChoice Group Ltd', 'MCZ : MC Mining Limited', 'MDI : Master Drilling Grp Ltd', 'MED : Middle East Diamond Res Ld', 'MEI : Mediclinic Int plc', 'MFL : Metrofile Holdings Ltd', 'MHB : Mahube Infrastructure Ltd', 'MIX : Mix Telematics Ltd', 'MKR : Montauk Renewables Inc', 'MMP : Marshall Monteagle plc', 'MNP : Mondi plc', 'MPT : Mpact Limited', 'MRF : Merafe Resources Ltd', 'MRI : Mine Restoration Inv Ltd', 'MRP : Mr Price Group Ltd', 'MSM : Massmart Holdings Ltd', 'MSP : MAS Real Estate Inc.', 'MST : Mustek Ltd', 'MTA : Metair Investments Ltd', 'MTH : Motus Holdings Ltd', 'MTM : Momentum Met Hldgs Ltd', 'MTN : MTN Group Ltd', 'MUR : Murray & Roberts Hldgs', 'N91 : Ninety One Plc', 'NCS : Nictus Ltd', 'NED : Nedbank Group Ltd', 'NFP : New Frontier Prop Ltd', 'NHM : Northam Platinum Ltd', 'NPK : Nampak Ltd', 'NPN : Naspers Ltd -N-', 'NRL : Newpark REIT Ltd', 'NRP : NEPI Rockcastle Plc', 'NT1 : Net 1 UEPS Tech Inc', 'NTC : Netcare Limited', 'NUT : Nutritional Holdings Ltd', 'NVE : NVest Financial Hldgs Ltd', 'NVS : Novus Holdings Limited', 'NWL : Nu-World Hldgs Ltd', 'NY1 : Ninety One Limited', 'OAO : Oando plc', 'OAS : Oasis Crescent Prop Fund', 'OCE : Oceana Group Ltd', 'OCT : Octodec Invest Ltd', 'OLG : Onelogix Group Ltd', 'OMN : Omnia Holdings Ltd', 'OMU : Old Mutual Limited', 'ORN : Orion Minerals Limited', 'PAN : Pan African Resource plc', 'PBG : PBT Group Limited', 'PEM : Pembury Lifestyle Grp Lt', 'PFB : Premier Fishing Brands Ltd', 'PIK : Pick n Pay Stores Ltd', 'PMV : Primeserv Group Ltd', 'PPC : PPC Limited', 'PPE : Purple Group Ltd', 'PPH : Pepkor Holdings Ltd', 'PPR : Putprop Ltd', 'PRX : Prosus N.V.', 'PSG : PSG Group Ltd', 'PSV : PSV Holdings Ltd', 'QFH : Quantum Foods Hldgs Ltd', 'QLT : Quilter Plc', 'RAV : Raven Property Group Ltd', 'RBP : Royal Bafokeng Platinum Ltd', 'RBX : Raubex Group Ltd', 'RCL : RCL Foods Limited', 'RDF : Redefine Properties Ltd', 'RDI : Rockwell Diamonds Inc', 'REA : Rebosis Property Fund Ltd A', 'REB : Rebosis Property Fund Ltd', 'REM : Remgro Ltd', 'REN : Renergen Limited', 'RES : Resilient REIT Limited', 'RFG : RFG Holdings Limited', 'RHB : RH Bophelo Limited', 'RLO : Reunert Ltd', 'RMH : RMB Holdings Ltd', 'RMI : Rand Merchant Inv Hldgs Ltd', 'RNG : Randgold & Expl Co Ltd', 'RNI : Reinet Investments S.C.A', 'RPL : RDI REIT P.L.C', 'RSG : Resource Generation Ltd', 'RTN : Rex Trueform Group -N-', 'RTO : Rex Trueform Group Ltd', 'S32 : South32 Limited', 'SAC : SA Corp Real Estate Ltd', 'SAP : Sappi Ltd', 'SAR : Safari Investments RSA Ltd', 'SBK : Standard Bank Group Ltd', 'SBP : Sabvest Capital Limited', 'SCD : Schroder Eur REIT plc', 'SCP : Stellar Cap Partners Ltd', 'SDO : Stadio Holdings Limited', 'SEA : Spear REIT Limited', 'SEB : Sebata Holdings Ltd', 'SEP : Sephaku Holdings Ltd', 'SFN : Sasfin Holdings Ltd', 'SHG : Sea Harvest Group Ltd ', 'SHP : Shoprite Holdings Ltd', 'SLM : Sanlam Limited', 'SNH : Steinhoff Int Hldgs N.V.', 'SNT : Santam Limited', 'SNV : Santova Logistics Ltd', 'SOH : South Ocean Holdings Ltd', 'SOL: Sasol Limited', 'SPA : Spanjaard Limited', 'SPG : Super Group Ltd', 'SPP : The Spar Group Ltd', 'SRE : Sirius Real Estate Ltd', 'SSK : Stefanuti Stck Hldgs Ltd', 'SSS : Stor-Age Prop REIT Ltd', 'SSW : Sibanye Stillwater Ltd', 'STP : Stenprop Limited', 'SUI : Sun International Ltd', 'SUR : Spur Corporation Ltd', 'SVB : Silverbridge Holdings', 'SYG : Sygnia Limited', 'TBS : Tiger Brands Ltd', 'TCP : Transaction Capital Ltd', 'TCS : Total Client Services Ld', 'TDH : Tradehold Ltd', 'TEX : Texton Property Fund Ltd', 'TFG : The Foschini Group Limited', 'TGO : Tsogo Sun Hotels LTD', 'THA : Tharisa plc', 'TKG : Telkom SA SOC Ltd', 'TLM : Telemaster Holdings Ltd', 'TMT : Trematon Capital Inv Ltd', 'TON : Tongaat Hulett Ltd', 'TPC : Transpaco Ltd', 'TPF : Transcend Res Prop Fd Ld', 'TRE : Trencor Ltd', 'TRL : Trellidor Hldgs Ltd', 'TRU : Truworths Int Ltd', 'TSG : Tsogo Sun Gaming Ltd', 'TTO : Trustco Group Hldgs Ltd', 'TWR : Tower Property Fund Ltd', 'TXT : Textainer Group Hldgs Ltd', 'UAT : Union Atlantic Minerals Ltd', 'UPL : Universal Partners Ltd', 'VIS : Visual International Hldgs Ltd', 'VKE : Vukile Property Fund Ltd', 'VLE : Value Group Ltd', 'VOD : Vodacom Group Ltd', 'VUN : Vunani Ltd', 'VVO : Vivo Energy plc', 'WBO : Wilson Bayly Hlm-Ovc Ltd', 'WEA : WG Wearne Ltd', 'WEZ : Wesizwe Platinum Ltd', 'WHL : Woolworths Holdings Ltd', 'WKF : Workforce Holdings Ltd', 'WSL : Wescoal Holdings Ltd', 'YRK : York Timber Holdings Ltd', 'ZCL : Zarclear Holdings Ltd', 'ZED : Zeder Inv Ltd']">
		</v-select>
	</div>

	<LineChart :data="msg" />
</template>

<script>
import axios from 'axios';
import LineChart from '../components/linechart.vue';
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';

export default {
	name: 'TimeSeries',
	components: {
        vSelect,
		LineChart
	},
	data() {
		return {
			msg: '',
			stock: '',
		};
	},
	methods: {
		getMessage() {
			const path = 'http://localhost:5000/stock?&s='.concat(this.stock.slice(0,3));
			axios.get(path)
				.then((res) => {
					this.msg = res.data;
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},
	},
	created() {
		this.stocks = ['NPN', 'MTN',];

	},
	watch: {
		stock() {
			if (this.stock.length > 2) {
				this.getMessage();
			}
		}
	}
};
</script>

<style>
.center {
	margin-left: auto;
	margin-right: auto;
	border-collapse: collapse;
}

.center td,
.center th {
	border: 1px solid #ddd;
	padding: 3px 10px 3px 10px;
}

.center tr:nth-child(even) {
	background-color: #f2f2f2;
}

.center tr:hover {
	background-color: #ddd;
}

.center th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #348bd6;
	color: white;
}

.flex-container {
	display: flex;
}

.flex-child {
	flex: 1;
}
</style>