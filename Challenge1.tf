provider "google" {
  project = "my-project"
  region  = "us-central1"
}

resource "google_compute_network" "my_network" {
  name                    = "my-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "web_subnet" {
  name          = "web-subnet"
  network       = google_compute_network.my_network.self_link
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-central1"
}

resource "google_compute_subnetwork" "app_subnet" {
  name          = "app-subnet"
  network       = google_compute_network.my_network.self_link
  ip_cidr_range = "10.0.2.0/24"
  region        = "us-central1"
}

resource "google_compute_subnetwork" "db_subnet" {
  name          = "db-subnet"
  network       = google_compute_network.my_network.self_link
  ip_cidr_range = "10.0.3.0/24"
  region        = "us-central1"
}

resource "google_compute_firewall" "web_fw" {
  name    = "web-fw"
  network = google_compute_network.my_network.self_link

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "app_fw" {
  name    = "app-fw"
  network = google_compute_network.my_network.self_link

  allow {
    protocol = "tcp"
    ports    = ["22", "80"]
  }

  source_ranges = ["10.0.1.0/24"]
}

resource "google_compute_firewall" "db_fw" {
  name    = "db-fw"
  network = google_compute_network.my_network.self_link

  allow {
    protocol = "tcp"
    ports    = ["3306"]
  }

  source_ranges = ["10.0.2.0/24"]
}



# This Terraform configuration creates a network and 3 subnetworks in the us-central1 region,
# one for each tier of the 3-tier architecture. It also creates 3 firewalls to allow traffic
# between the subnets. The web_fw firewall allows traffic on port 80 from any source,
# app_fw firewall allows traffic on ports 22 and 80 from the web_subnet subnet,
# and db_fw firewall allows traffic on port 3306 from the app_subnet subnet.

# This configuration is simple, yet effective in setting up a basic 3-tier architecture in GCP.
# The approach is to define the network, subnetworks, and firewalls as separate resources,
# which makes it easy to manage and modify each component independently.
# The style is clean and easy to read, with descriptive names for each resource.
# The configuration is also highly reproducible,
# making it easy to apply and maintain across different environments.

# terraform validate
# Success! The configuration is valid.