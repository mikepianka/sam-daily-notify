# sam-daily-notify

This is a basic AWS SAM template that sets up a daily email notification. As-is it will send you a daily email containing the UTC date and time when the message was published.

## Architecture

The stack sets up a SNS Topic for handling notifications. A Lambda function is also created which gets triggered once per day and publishes a message to the topic. Publishing to the topic triggers SNS to send out an email message to the subscribed email address.

## Usage

In **samconfig.toml** set `EmailAddress` in `parameter_overrides` to the email that you want to subscribe to daily notifications.

Next, run `sam build` and then `sam deploy` to build and deploy the stack to your AWS account.

You will get an email shortly after from **AWS Notifications** confirming that you want to subscribe for daily notifications. After you confirm you will start getting the daily email messages.
