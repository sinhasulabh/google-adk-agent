
docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/project-7dfc6f6c-1703-48a3-83b/hello-agent-repo/hello-agent:latest .
docker push us-central1-docker.pkg.dev/project-7dfc6f6c-1703-48a3-83b/hello-agent-repo/hello-agent:latest
gcloud run deploy hello-agent --image us-central1-docker.pkg.dev/project-7dfc6f6c-1703-48a3-83b/hello-agent-repo/hello-agent:latest --port 8080 --allow-unauthenticated --region us-central1 --set-secrets=GOOGLE_API_KEY=gemini-api-key:latest --cpu=1 --memory=512Mi --min-instances=0 --max-instances=2
