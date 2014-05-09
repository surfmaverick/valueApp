__author__ = 'chris'

'''
This application will produce a cash flow analysis for a single asset.  We will start with a wind asset and then
build out other sources of generation.  The application is designed to work within Microsoft Excel as a front end
also on a stand alone basis so that users have optionality with respect to how they interface the system.

there will be a series of modules:
1.  operating cash flows
       - production (volumetric)
           inputs:
               fuel(with an s - for example, with multiple fuels combusted )
               production
               starts


           outputs:
               emissions
                   nox, sox, co2, halides, dioxins, mercury, arsenic
               energy
                   hourly
               renewable energy
               transmission rights
               capacity
                   hourly
               discharge
                   ash, water, hazardous waste

       - revenues:
           - volumetric driven (wind, solar, hydro, nuclear, geothermal, energy efficiency, solid fuel) for all or a
           portion
           - capacity based (solid fuel, gas turbine, geothermal, hydro, solar, nuclear) for all or a portion
           - other (time based, for example)

           each revenue line will need to be separately configurable so that it applies to some percentage
           of generation or to generation

       - variable expenses:
            volumetric:
                each with its own logic and label:
                   run hours
                   MWh
                   basis (power, fuels, water, emissions)

            revenue based:
                each with its own logic and label:
                    revenues earned
                    net revenues earned
                    net cash flow

        - fixed expenses:
                each with its own logic and label:
                   fixed by month, quarter, year, or season

        - hybrid expenses (hybrid expenses have a cost that is somewhat variable but bounded by certain fixed
         constraints. An example of this would be lease payments that are payment according to a volumetric amount
         but have a fixed periodic minimum)
                each with its own logic

           maintenance:
               regular  maintenance (maintenance that is performed at regular calendar intervals)
               interval maintenance (maintenance that is performed according to some volumetric driver (time in
               service, hours run, mwh generated or etc)

        - working capital


   questions to be sorted out:
        - how will rules be defined?  Unique to each item, with a standard menu of rules only, or something in
        between
        - can users add their own rules for operation to any item (ntd: probably the latter)?
        - should everything be calculated hourly and then rolled up?
        - should the model work with ten minute data and roll up from there?
        - each expense should have its own category or property based upon object properties.  The expense would
        then be applied based upon the operations profile of the asset according to the rules
        - what is the best way to setup the rules?

2.  financing
        - debt model
           floating rate loans
               regular way commercial bank debt
               sculpted commercial bank debt
               term loan b, sculpted
               lines of credit

           notes and other fixed rate instruments
               144a notes
               4(2) notes
               public notes

            swaps
                sculpted
                linear
                flexible

            mezzanine
                classes
                costs


        - equity model
            equity timing - first, last, pro rata
            classes of equity:
                different subordination rights might apply
                warrants?


        - waterfall rules:
            the waterfall has to be properly configured so that the cash flows map correctly through the model.
            For example, the cash flow has to be configured properly so that forms of debt cash flows are dealt
            with properly.  Each class of debt should have its own set of rules but there should be a general
            set of rules that define constraints that apply to all classes.  For example, "debt" payments
            should not start until a project construction is completed, however a fixed rate note might have an
            override to PIK or cash pay during construction (with a negative spread), but commercial bank
            debt might just accrue


      topical notes
           The debt model is very complicated because it is at the heart of the valuation of financial cash flows
           and conditions of the loan itself being used for application, and the variable nature of the underlying
           interest rate model

           The key variables are:
               - interest rates
               - coverages
               - sizing

       - refinancing debt model
           time period
           fees
           settlement of existing instruments
           interest rate risk
           constraints on refinancing
               debt to total capital
           instrument mix as a percentage of total financing


3.  reporting/accounting/cash flows
        income statement
        balance sheet (including book/tax differences)
        operating cash flow
        debt cash flows
        equity cash flows
        sources/uses
        operating expenses by:
            type
            ratio to production
            monthly/annually/quarterly

4.  tax
    partnership flip economics to include:
        discrete adjustments
        capital account maintenance in good order
    sale/leaseback economics
        sale/leaseback optimization

5.  risk reporting and analysis
    volumetric risk
    operating risk
    inflation and financial risk
    construction cost overrun
    price risk for any item

6. Risk scenarios
    changing assumptions to evaluate impacts
    reporting of results

Each of these modules will be designed to interface with a central asset model, but the program should be smart enough
not to require rerun of the core operations folder unless something has changed in the original assumptions from the
last run.

The application will run a cash flow profile working down to EBITDA, and then including major maintenance and working capital.

Module definitions:

Operations()
asset(   ) -- defines the asset each with a series of discrete properties
    type of asset (wind, solar, etc)
    constructed or to be built
    start date
    operating date
    operating term (does it matter whether we start with monthly calculation or should we start with days and roll it up)
    revenue sources
    expense sources
    liability sources
    equity sources
    inputs
    outputs
    dispatch rules

construction ( )
    - item
    - timing rule
    - category

operations (    )
    - start date
    - end date

revenue (    ) -- defines the expected revenues configured as a series
    - source
    - amounts
    - calculation (volumetric, fixed, etc)
    - timing rules

input(  )
    - type (asset or liability)
    - calculation or timing rule
    - cost

output(   )
    - type (asset or liability)
    - cost
    - calculation or timing rule

Financing()

Liability()
    - type
    - cost
    - ranking
    - calculation methodology

preferred equity( )
    - type
    - coupon
    - payment rules

common euqity( )
    - type


'''
