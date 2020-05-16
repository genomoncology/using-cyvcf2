from cyvcf2 import VCF
from functions import display_obj_values


def examine_spec():
    print("\nspec.vcf\n")

    vcf = VCF("./spec.vcf")

    print("\nDisplay VCF:\n")
    display_obj_values(vcf)

    print("\nDisplay Variant:\n")
    first_variant = next(vcf)
    display_obj_values(first_variant)
    print("\n")


def examine_vaf():
    print("\nvaf.vcf\n")

    vcf = VCF("./vaf.vcf")

    print("\nDisplay VCF:\n")
    display_obj_values(vcf)

    print("\nDisplay Variant:\n")
    first_variant = next(vcf)
    display_obj_values(first_variant)
    print("\n")


if __name__ == "__main__":
    examine_spec()
    examine_vaf()
