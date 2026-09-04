# Week 3 Task: Advanced Data Analysis and Visualization in Logistics

## Executive Summary
This project provides an exploratory data analysis (EDA) of supply chain logistics using Python. It identifies key operational cost drivers, quantifies delivery delays, and evaluates carrier reliability across 1,000 simulated shipment records.

## Project Structure
- `logistics_analysis.py`: Python script for dataset simulation, EDA, statistical modeling, and plot generation.
- `Logistics Data Analysis Report - Week 3 Task.docx`: Comprehensive written documentation detailing methodology, findings, and strategic recommendations.

## Methodology & Variables
Data was synthesized using `pandas` and `numpy` to evaluate key metrics:
- **Shipment_ID**: Unique tracking code.
- **Carrier**: Delivery partner (Carrier A, Carrier B, Carrier C).
- **Distance_km**: Total transit distance (100–2500 km).
- **Shipment_Weight_kg**: Cargo weight (10–500 kg).
- **Delay_Days**: Variance between actual and planned delivery dates.
- **Transportation_Cost_USD**: Calculated based on base rate ($50), distance ($0.45/km), weight ($0.85/kg), and delay surcharges ($30/day).

## Key Findings
1. **Primary Cost Drivers**: Distance and cargo weight account for over 80% of transportation cost variance. Unplanned delays add an average penalty surcharge of $30/day per shipment.
2. **Carrier Performance**: Carrier A maintained high schedule reliability (>85% on-time rate). Carrier C was identified as the main operational bottleneck, causing delays up to 5 days.
3. **Route Friction**: Long-distance shipments (>1,800 km) via Hub East experienced a 42% delay rate.

## Strategic Recommendations
- Reallocate 15–20% of shipment volume from Carrier C to Carriers A and B.
- Implement dynamic routing software to bypass bottleneck transit hubs (Hub East).
- Consolidate smaller, high-frequency shipments to maximize weight-to-cost efficiency.
