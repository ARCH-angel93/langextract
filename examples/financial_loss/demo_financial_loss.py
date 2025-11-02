#!/usr/bin/env python3
# Copyright 2025 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demo: Financial Loss ("Lost Wealth") Extraction with LangExtract.

This example demonstrates how to use LangExtract to extract structured
information about financial losses from text documents. It extracts:
- Loss amounts and affected entities
- Loss causes and time periods
- Financial events and their context

Usage:
    python demo_financial_loss.py

Note: This example is for demonstration purposes only and does not
constitute financial advice.
"""

import langextract as lx


def main():
  """Run the financial loss extraction demo."""

  # Define the extraction prompt
  prompt_description = """Extract financial loss information including:
  - Loss events (what was lost)
  - Loss amounts (monetary values)
  - Loss causes (why the loss occurred)
  - Time periods (when the loss happened)
  - Affected entities (who experienced the loss)

  Use exact text for extractions. Do not paraphrase or overlap entities.
  Provide meaningful attributes for each entity to add context."""

  # Provide high-quality examples to guide the model
  examples = [
      lx.data.ExampleData(
          text="The company reported a $2.5 million loss in Q3 2023 due to market volatility and poor investment decisions.",
          extractions=[
              lx.data.Extraction(
                  extraction_class="affected_entity",
                  extraction_text="The company",
                  attributes={"type": "organization"}
              ),
              lx.data.Extraction(
                  extraction_class="loss_amount",
                  extraction_text="$2.5 million loss",
                  attributes={"currency": "USD", "value": "2500000"}
              ),
              lx.data.Extraction(
                  extraction_class="time_period",
                  extraction_text="Q3 2023",
                  attributes={"quarter": "Q3", "year": "2023"}
              ),
              lx.data.Extraction(
                  extraction_class="loss_cause",
                  extraction_text="market volatility",
                  attributes={"category": "market_conditions"}
              ),
              lx.data.Extraction(
                  extraction_class="loss_cause",
                  extraction_text="poor investment decisions",
                  attributes={"category": "management_decisions"}
              )
          ]
      )
  ]

  # Example text about financial losses
  input_text = """John Smith lost $50,000 in the stock market crash of 2024.
  The losses were primarily from tech stocks that declined sharply in March.
  
  Meanwhile, ABC Corporation reported $1.8 million in losses during Q1 2024
  attributed to supply chain disruptions and increased operational costs."""

  print("=" * 70)
  print("Financial Loss Extraction Demo")
  print("=" * 70)
  print("\nInput Text:")
  print("-" * 70)
  print(input_text)
  print("-" * 70)

  # Run the extraction
  print("\nRunning extraction with LangExtract...")
  print("(Note: This requires a valid API key for Gemini)")

  try:
    result = lx.extract(
        text_or_documents=input_text,
        prompt_description=prompt_description,
        examples=examples,
        model_id="gemini-2.5-flash",
    )

    # Display results
    print("\n✓ Extraction completed!")
    print(f"Found {len(result.extractions)} financial entities:\n")

    for i, extraction in enumerate(result.extractions, 1):
      print(f"{i}. {extraction.extraction_class}: '{extraction.extraction_text}'")
      if extraction.attributes:
        for key, value in extraction.attributes.items():
          print(f"   - {key}: {value}")
      print()

    # Save results
    output_file = "financial_losses.jsonl"
    print(f"\nSaving results to {output_file}...")
    lx.io.save_annotated_documents(
        [result],
        output_name=output_file,
        output_dir="."
    )
    print(f"✓ Results saved to {output_file}")

    # Generate visualization
    print("\nGenerating interactive visualization...")
    html_content = lx.visualize(output_file)
    viz_file = "financial_losses_viz.html"
    with open(viz_file, "w", encoding="utf-8") as f:
      if hasattr(html_content, 'data'):
        f.write(html_content.data)
      else:
        f.write(html_content)
    print(f"✓ Visualization saved to {viz_file}")
    print("\nOpen the HTML file in a browser to explore the extractions!")

  except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nMake sure you have:")
    print("1. Set LANGEXTRACT_API_KEY environment variable")
    print("2. Or created a .env file with your API key")
    print("3. Or pass api_key parameter to lx.extract()")
    return 1

  return 0


if __name__ == "__main__":
  import sys
  sys.exit(main())
