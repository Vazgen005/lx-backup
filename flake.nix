{
  description = "ROSA-backup Python package";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python3Packages;
      in {
        packages.default = pythonPackages.buildPythonPackage {
          name = "lx-backup";
          version = "0.1.0";  # You should specify a version
          src = ./.;
          propagatedBuildInputs = with pythonPackages; [
            pyside6
            human-readable
          ];
          format = "pyproject";
          nativeBuildInputs = with pythonPackages; [
            hatchling
          ];
        };

        devShells.default = pkgs.mkShell {
          buildInputs = with pythonPackages; [
            pyside6
            human-readable
            hatchling
            pkgs.poethepoet
          ];
        };

        apps = {
          lx-backup = {
            type = "app";
            program = "${self.packages.${system}.default}/bin/rosa-backup";
          };
          default = self.apps.${system}.lx-backup;
        };
      });
}
