import fintech as ft
import datetime as date

# Testing program
if __name__ == "__main__":
    print("Unit tests initiated...\n")
    try:
        ICs, weights = ft.GetICsAndWeights(date.datetime(2017, 9, 15), "ALSI")
        print("F1: GetICsAndWeights - test passed successfully")
        betas, specVols, mktVol = ft.GetBetasMktAndSpecVols(date.datetime(2017, 9, 15), ICs, "J203")
        print("F2: GetBetasMktAndSpecVols - test passed successfully")
        pfBeta, sysCov, pfSysVol, ft.specCov, pfSpecVol, totCov, pfVol, corrMat = ft.CalcStats(weights, betas, mktVol, specVols)
        print("F3: CalcStats - test passed successfully")
        stockdata = ft.getTimeSeries("PRX")
        print("F4: getTimeSeries - test passed successfully")
        pfData = ft.GetPricesAndWeights(['CPI'],[1])
        print("F5: GetPricesAndWeights - test passed successfully")
        stocks = ft.GetEquitiesList()
        print("F6: GetEquititiesList - test passed successfully")
        pfBeta, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, corrMat = ft.customPfStats(['MTN', 'CPI'], [0.2, 0.8], "J203")
        print("F7: customPfStats - test passed successfully")
        print("\nAll tests completed successfully.")

    except:
        print("Test failed")
    