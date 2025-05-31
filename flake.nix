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
          name = "ROSA-backup";
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

        # Optional: Add a devShell for development
        devShells.default = pkgs.mkShell {
          buildInputs = with pythonPackages; [
            pyside6
            human-readable
            hatchling
          ];
        };
      });
}
