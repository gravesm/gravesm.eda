# Declared State & Event Driven Ansible Collection

This is a proof of concept collection for demonstrating the ability to use [ansible-events](https://github.com/benthomasson/ansible-events) to react to changes in AWS infrastructure. The goal is to begin with a defined state of resources managed by Ansible. As changes to those resources occur, ansible-events reacts by returning the resources to their initial defined state.

The collection contains a continuation of some of the earlier work on [a declared state Ansible experiment](https://github.com/gravesm/gravesm.cloud), plus some plugins for handling remediation.
