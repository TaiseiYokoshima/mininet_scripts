#!/usr/bin/env bash
vm="ubuntu20.04"

ip=$(virsh domifaddr $vm | grep -Eo '192\.168\.[0-9]{1,3}\.[0-9]{1,3}')

ssh "mininet@$ip"


