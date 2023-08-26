# TimerTrigger - Python

The `TimerTrigger` makes it incredibly easy to have your functions executed on a schedule. This sample demonstrates a simple use case of calling your function every 5 minutes.

## How it works

For a `TimerTrigger` to work, you provide a schedule in the form of a [cron expression](https://en.wikipedia.org/wiki/Cron#CRON_expression)(See the link for full details). A cron expression is a string with 6 separate expressions which represent a given schedule via patterns. The pattern we use to represent every 5 minutes is `0 */5 * * * *`. This, in plain text, means: "When seconds is equal to 0, minutes is divisible by 5, for any hour, day of the month, month, day of the week, or year".

## Learn more

<TODO> Documentation

Some resources to follow:

# Development

## Selenium and Beautifulsoup and Python

https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25

## Azure Functions Python developer guide:

https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-configuration

## timer-triggered-azure-functions with keyvault to add configuration values:

https://www.bizstream.com/blog/timer-triggered-azure-functions-in-c-with-net-6/
https://beetechnical.com/cloud-computing/http-trigger-azure-function/#google_vignette

# Testing

## For testing locally need to install Azurite extension and configure the extension setting for VS Code:

https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=visual-studio-code

## For issue:

https://stackoverflow.com/questions/70764836/timetrigger-exception-could-not-create-blobcontainerclient-for-schedulemonitor

## Try this sample to create loop in selenium

https://stackoverflow.com/questions/71480545/how-to-stop-the-selenium-webdriver-after-reaching-the-last-page-while-scraping-t

## azure function and service bus queue

https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output?tabs=python-v1%2Cin-process%2Cextensionv5&pivots=programming-language-python
