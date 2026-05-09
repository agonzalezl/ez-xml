"""Convert Peppol Schematron .sch files to .xsl using ISO Schematron XSLT pipeline"""

import os
import tempfile
from pathlib import Path

from saxonche import PySaxonProcessor


def convert_sch_to_xsl(sch_file, xsl_file):
    """Convert .sch to .xsl using ISO Schematron XSLT pipeline"""
    base_dir = Path(sch_file).parent
    sch_file = Path(sch_file)
    xsl_file = Path(xsl_file)

    with PySaxonProcessor(license=False) as proc:
        xslt = proc.new_xslt30_processor()

        # Use temp files for intermediate steps
        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as tmp1:
            tmp1_path = tmp1.name
        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as tmp2:
            tmp2_path = tmp2.name

        try:
            # Step 1: Expand inclusions (iso_dsdl_include.xsl)
            step1_xsl = str(base_dir / "iso_dsdl_include.xsl")
            result1 = xslt.transform_to_string(
                source_file=str(sch_file), stylesheet_file=step1_xsl
            )
            Path(tmp1_path).write_text(result1, encoding="utf-8")

            # Step 2: Expand abstract patterns (iso_abstract_expand.xsl)
            step2_xsl = str(base_dir / "iso_abstract_expand.xsl")
            result2 = xslt.transform_to_string(
                source_file=tmp1_path, stylesheet_file=step2_xsl
            )
            Path(tmp2_path).write_text(result2, encoding="utf-8")

            # Step 3: Generate XSLT (iso_svrl_for_xslt2.xsl)
            step3_xsl = str(base_dir / "iso_svrl_for_xslt2.xsl")
            result3 = xslt.transform_to_string(
                source_file=tmp2_path, stylesheet_file=step3_xsl
            )

            # Save final XSLT
            xsl_file.write_text(result3, encoding="utf-8")
            print(f"Converted {sch_file.name} -> {xsl_file.name}")
        finally:
            # Cleanup temp files
            for f in [tmp1_path, tmp2_path]:
                if os.path.exists(f):
                    os.unlink(f)


if __name__ == "__main__":
    base = Path(__file__).parent
    convert_sch_to_xsl(base / "PEPPOL-EN16931-UBL.sch", base / "PEPPOL-EN16931-UBL.xsl")
    convert_sch_to_xsl(base / "CEN-EN16931-UBL.sch", base / "CEN-EN16931-UBL.xsl")
