# FAQs

Here are some frequently asked questions (FAQs) about IEX Cloud.

## Account, Billing, and Pricing

### How can I make changes to my plan?

You can request upgrading, downgrading, or cancelling your subscription at any time via the console's [Manage Plan](https://iexcloud.io/console/manage-plan) page.

### When do plan upgrades take affect?

When you upgrade your plan, the new subscription goes into effect immediately.

### When do plan downgrades take affect?

We don't provide prorated refunds for downgrades or cancellations. When you downgrade or cancel, you will remain on your higher-tier subscription through the end of your current term. You can see your current term's next renewal date in the console's [Billing](https://iexcloud.io/console/billing) section. Once your next renewal date comes around, you will automatically be placed on your downgraded subscription. 

### (Legacy) Can I add or remove packages on my legacy plan?

You can both add and remove packages from a legacy plan as needed. Once you add a package, by default, it will be added to your plan for each subsequent month. If you remove a package from your plan, it expires at the end of the current month. Packages can be removed or added month to month for any paid legacy plan.

## Data

### What usage restrictions and requirements do the various plans have?

Users on the Start Plan (legacy) are only permitted to use data from IEX Cloud for personal, non-commercial use. Paid plan users can use IEX Cloud data for commercial use, including displaying publicly to users.

No user may provide IEX Cloud data via their own API to users, or provide a mechanism for mass downloads, for example as a CSV. For more information please see our terms of service.

Attribution is required for all users. It is as simple as putting “Data provided by IEX Cloud” somewhere on your site or app and linking that text to <https://iexcloud.io>.

### How do I get data on the S&P 500, Dow Jones Industrial Average, or other major stock indices?

Data on major stock indices is not currently available on IEX Cloud

Data on the S&P 500, Dow Jones Industrial Average, and other major stock indices is not currently available on IEX Cloud and is unlikely to be in the near future.

Pricing for this data is typically high and requires a direct contract between each consumer and the index provider regardless of who actually supplies the data. For instance, the major index providers charge over $10,000 a year for delayed data.

An alternative is to display ETFs that match those indices, such as SPY for the S&P 500, DIA for Dow Jones, and IWM for Russell 2000.


**Restrict Domains For Calls Made With A Publishable Key**

Please see [Restricting Data Access to Specific Domains](./administration/access-and-security/restricting-data-access-to-specific-domains.md).

### How do I get Nasdaq-listed stock data (UTP/OTC Data) on IEX Cloud?

Please see [Getting Nasdaq-listed UTP/OTP Stock Data](./using-core-data/getting-nasdaq-listed-utp-otc-stock-data.md).

### How do I stream in data?

Please see [Streaming Data Using SSE](using-core-data/streaming-data-using-sse.md).

### (Legacy) How do I enable access to earnings and estimates Data?

There is global coverage of earnings and estimates data. Due to this third-party provider terms of use, however, the data requires additional entitlements and in certain scenarios must be accessed from the data partner directly. Affected endpoints include:

- [Estimates](https://iexcloud.io/docs/api/#estimates)
- [Earnings](https://iexcloud.io/docs/api/#earnings)
- [Earnings Today](https://iexcloud.io/docs/api/#earnings-today)
- [Price Target](https://iexcloud.io/docs/api/#price-target)
- [Analyst Recommendations](https://iexcloud.io/docs/api/#analyst-recommendations)

**If you are planning on using this data for personal or internal use only** – with no redistribution or redisplay – simply follow the instructions below to access this data.

These endpoints will be included in the Marketplace section for entitlement purposes. All usage will use pay-as-you-go credits (legacy) or Premium Data credits, but the data weights and endpoint URLs will remain unchanged.

**If you would like to redistribute this data**, such as redisplaying data on a public-facing website or application, you will need to negotiate an agreement directly with our data partner. Please reach out to our partnerships team at <partners@iexcloud.io> if you would like us to make that introduction.

**Here’s how the entitlement process works:**

Head to the [Marketplace tab in the IEX Cloud Console](https://iexcloud.io/console/marketplace) and request access to “Earnings, Estimates, Price Targets, and Analyst Recommendations.”

You will be asked to provide basic information about who you are and how you will be using the data. Once approved, you will be able to use these endpoints. Access requests will typically be reviewed in 1-2 business days. Our team will reach out if we need additional information.

The number of credits per API call is not changing. However, API calls for these endpoints will use pay-as-you-go credits (legacy) or Premium Data credits, rather than the core credits included with your plan. This means that usage of these endpoints will be billed each month in addition to your base subscription charges.

Questions? Reach out to <support@iexcloud.io> for assistance.

## General

### Can I redisplay/ redistribute the data I receive from IEX Cloud?

In general, displaying IEX Cloud data is permitted with attribution. The following are some restrictions on the use of IEX Cloud data:

- Users on the Start plan are only permitted to use data from IEX Cloud for personal, non-commercial use. You can still display data to other individuals/users, but you may not include our data in any commercial application. Paid plan users can use IEX Cloud data for commercial use, including displaying publicly to users.
- No user may provide IEX Cloud data via their own API to users, or provide a mechanism for mass downloads, for example as a CSV. For more information please see our terms of service.
- Attribution is required for all users. If a customer distributes IEX Cloud Data, they must state that the data was provided by IEX Cloud and provide a hyperlink to <https://iexcloud.io>.

For more information, please see the Acceptable Use Policy within our Terms: <https://iexcloud.io/terms/#aup>.