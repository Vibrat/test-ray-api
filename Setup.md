# Set up Ray projects

```bash
kind create cluster --image=kindest/node:v1.26.0
helm install kuberay-operator  kuberay/kuberay-operator --version 1.2.2
helm install raycluster kuberay/ray-cluster --version 1.2.2 --set 'image.tag=2.9.0-aarch64'
```

## Deployment for normal application

```bash
pip install "ray[serve]"
```