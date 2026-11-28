# Sources: Puerto Rico power-bill protest (BREAKING, Nov 27, 2026)

## Story
- **AP**, Dánica Coto & Alejandro Granadillo, "Protesters take to the streets in Puerto Rico's capital as standard of living deteriorates," Nov 27, 2026.
  https://apnews.com/article/puerto-rico-protest-water-power-luma-san-juan-282de19fa396ef0c8bcf276499486578
  - apnews.com returned HTTP 403 / timeout to WebFetch and curl. Full AP wire text verified via the AP-credited reprint in the Jamaica Gleaner (byline "SAN JUAN, Puerto Rico (AP)"):
    https://jamaica-gleaner.com/article/world-news/20261127/protesters-take-streets-puerto-ricos-capital-standard-living
  - Verified AP text used: "Thousands of people protested Friday in Puerto Rico's capital as anger and frustration erupted over record-high electric rates, the surging cost of living, deterioration in basic services"; "some 30 groups"; "largest mall in the Caribbean on Black Friday"; "Day of National Outrage"; "Monthly electricity bills for some residential customers recently rose about 18%, from $229 to $271"; "On Wednesday, Puerto Rico's Supreme Court narrowly approved canceling the government's contract with Luma. The governor praised the ruling"; Association of Industries: cancellation could "discourage private investment and jeopardize the continuity of projects in progress."
- **EFE**, "Miles de manifestantes cortan una de las principales vías de Puerto Rico en Viernes Negro," Nov 27, 2026 (fetched OK).
  https://efe.com/economia/2026-11-27/puerto-rico-protestas-viernes-negro-indignacion-servicios/
  - "Más de 4.000 manifestantes ... cortaron ... el Expreso Las Américas"; "más de 30 organizaciones"; "incremento del 18,5 % en la tarifa de la luz en el último trimestre"; ~143,000 public pensioners, 55,000+ under $1,000/month; Fiscal Oversight Board said service "debe ser administrado por un operador privado"; Dept. of Public Safety reported progress on firefighters' demands (pending FOMB approval).
- **Tribunal Supremo de Puerto Rico** press release, Nov 25, 2026 (fetched OK): voided LUMA contract extension 5-4; orderly transition within the one-year contractual term under Court of First Instance supervision. Cases CT-2025-0006 / CT-2025-0007.
  https://poderjudicial.pr/tribunal-supremo-declara-nula-la-extension-de-la-relacion-contractual-con-luma-energy-y-dispone-una-transicion-ordenada/
- AP background, LUMA Supreme Court story (403 to fetch; not relied on for any number): https://apnews.com/article/puerto-rico-luma-supreme-court-power-energy-e45076fdebfe5c07de142dcb05f771c2

## Primary data (card chart)
- **U.S. EIA, Form EIA-861M "Sales and revenue" (sales_revenue.xlsx)**, downloaded Nov 27, 2026, https://www.eia.gov/electricity/data/eia861m/xls/sales_revenue.xlsx (copy in data/)
  - Sheet "Monthly-Ter", 2026-09, PR, Preliminary: Residential price **25.15 cents/kWh** (revenue $197,078.49K / 783,759.95 MWh; 1,389,412 customers).
  - Sheet "US-YTD", 2026-09, Preliminary: U.S. residential price **18.168 cents/kWh** (rounded 18.17).
- **EIA Electric Power Monthly Table 5.6.A** (September 2026): U.S. Total residential **18.17** cents/kWh (matches 861M). Puerto Rico is not in Table 5.6.A (50 states + DC only), which is why 861M "Monthly-Ter" is used for PR.
  https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a

## Numbers used
| Number | Where | Source |
|---|---|---|
| 25.15¢/kWh PR residential, Sept 2026 | card | EIA-861M, Monthly-Ter, preliminary |
| 18.17¢/kWh U.S. residential, Sept 2026 | card | EIA-861M US-YTD / EPM Table 5.6.A |
| ~18% bill rise | tweet | AP (Gleaner reprint) |

## Not used / caveats
- AP's "$229 to $271" and "33.86 cents per kWh" (a new tariff rate) vs "18.3 cents ... U.S. mainland, according to EIA" appear in AP text, but 33.86¢ is a current tariff rate while EIA's are realized average prices for a past month; not mixed on the card. AP's 18.3¢ EIA figure doesn't match EIA's Sept 2026 18.17¢ (likely a different month or period); not used.
- Crowd size: EFE 4,000+; organizers (per El Nuevo Día, via Condado Daily) 8,000+; AP "thousands." Card/tweet say "thousands."
- No LUMA statement on the protest found in AP or EFE.
