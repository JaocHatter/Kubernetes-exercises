# Kubernetes, monitoreo 

## Uso de docker para pruebas locales

![alt text](img/img1.png)

## Despliegue de Kubernetes
1. Crear un namespace donde trabajar
![alt text](img/img2.png)

2. Sube la imágen de tu proyecto a Dockerhub.
```bash 
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname
```
![alt text](img/img4.png)

3. Crea un manifesto para poder crear 3 pods, cada uno con un contenedor de la aplicación.

![alt text](img/img3.png)
## Observabilidad completa

Comenzamos con la instalación de Prometheus para la recolección de métricas en nuestro Stack de Observación.

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

help repo update

helm install prometheus prometheus-community/prometheus -n observability
```
![alt text](img/img5.png)


Instalación de grafana

```bash
helm repo add grafana https://grafana.github.io/helm-charts

help repo update

helm install grafana grafana/grafana -n observability --set adminPassword='admin'
```
![alt text](img/img6.png)

**Verificar la instalación**
```bash
kubectl get pods -n observability
```

![alt text](img/img7.png)

**Redirigir puertos locales**

Redirecciona los puertos locales, en este caso redirecciona el puerto 3000 del host al puerto 80 de los kubernetes.

```bash
kubectl port-forward svc/grafana 3000:80 -n observability
```
![alt text](img/img8.png)

Grafana en el puerto 3000

![alt text](img/img9.png)

## Obtener las Golden Signals

![alt text](img/img10.png)
