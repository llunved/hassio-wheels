[![Build Status](https://dev.azure.com/home-assistant/Hass.io/_apis/build/status/wheels?branchName=master)](https://dev.azure.com/home-assistant/Hass.io/_build/latest?definitionId=11&branchName=master)


# CONTAINER BUILD
```
export HWARCH=$(uname -m); sudo podman build --net=host --build-arg BUILD_FROM=fedora:28 --build-arg BUILD_ARCH=${HWARCH} -t hass-f28-${HWARCH}-builder -f Dockerfile.Fedora .
```

# Hass.io Wheels builder

```sh

$ python3 -m builder \
    --apk build-base \
    --index https://wheels.home-assistant.io \
    --requirement requirements_all.txt \
    --upload rsync \
    --remote user@server:/wheels
```

## Supported file transfer

- rsync

## Folder structure of index folder:

`/alpine-{version}/{arch}/*`
