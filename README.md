# flask-email-notifier

This project is a Flask application that sends email notifications. Follow the steps below to deploy it to an Rahti2 OpenShift cluster.

## Deployment Steps

### 1. Create a New Project
First, create a new project in OpenShift:
```sh
oc new-project smtp-project --description="csc_project:200xxxx"
```

### 2. Deploy the Application
Use the following command to deploy the application:
```sh
oc new-app https://github.com/jemaltahir/flask-email-notifier.git --strategy=docker --name="smtp" -l app=smtp
```

### 3. Set Environment Variables
Set the necessary environment variables for the deployment:
```sh
oc set env deployment/smtp SENDER_EMAIL=your-email@gmail.com RECEIVER_EMAIL=receiver-email@gmail.com
```

### 4. Manually Trigger a Build
```sh
oc start-build smtp
```

### 5. Check OpenShift Logs for Errors
```sh
oc logs bc/smtp
```

### 6. Deploy service and Routes
```Sh
oc apply -f service.yaml
oc apply -f route.yaml
```